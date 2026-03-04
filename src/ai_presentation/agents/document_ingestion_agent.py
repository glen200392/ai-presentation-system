"""Document Ingestion Agent for parsing documents and URLs into structured content."""

import logging
import os
from typing import Any, Dict, List, Optional
from .base_agent import BaseAgent

logger = logging.getLogger(__name__)


def _count_words(text: str) -> int:
    return len(text.split()) if text else 0


def _split_sections(text: str) -> List[str]:
    """Split text into rough sections by blank lines or headings."""
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    return paragraphs[:10]  # cap at 10 sections


class DocumentIngestionAgent(BaseAgent):
    """Parses PDF, DOCX, plain text, and URLs into structured content."""

    name = "DocumentIngestion"

    def __init__(self, config: Optional[Dict[str, Any]] = None):
        super().__init__(self.name, config or {})
        logger.info("DocumentIngestionAgent initialized")

    async def execute(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """Execute document ingestion."""
        source = input_data.get("source", "")
        return await self.ingest(source)

    async def ingest(self, source: str) -> Dict[str, Any]:
        """
        Ingest a document or URL and return structured content.

        Args:
            source: File path (PDF/DOCX/TXT/MD) or URL string

        Returns:
            dict with keys: source_type, raw_text, title, word_count, sections
        """
        if not source:
            return self._empty_result("unknown")

        if source.startswith("http://") or source.startswith("https://"):
            return await self._ingest_url(source)

        ext = os.path.splitext(source)[1].lower()
        if ext == ".pdf":
            return await self._ingest_pdf(source)
        elif ext == ".docx":
            return await self._ingest_docx(source)
        else:
            return await self._ingest_text(source)

    async def _ingest_url(self, url: str) -> Dict[str, Any]:
        """Fetch and extract main body text from a URL."""
        try:
            import requests
            from bs4 import BeautifulSoup

            response = requests.get(url, timeout=15)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "lxml")

            # Remove script and style elements
            for tag in soup(["script", "style", "nav", "footer", "header"]):
                tag.decompose()

            title = (
                soup.title.string.strip() if soup.title and soup.title.string else url
            )
            raw_text = soup.get_text(separator="\n", strip=True)

            self.log_info(f"Ingested URL: {url} ({_count_words(raw_text)} words)")
            return self._build_result("url", raw_text, title)
        except Exception as e:
            self.log_error(f"Failed to ingest URL {url}: {e}")
            return self._empty_result("url")

    async def _ingest_pdf(self, path: str) -> Dict[str, Any]:
        """Extract text from a PDF file."""
        try:
            import PyPDF2

            raw_text = ""
            with open(path, "rb") as f:
                reader = PyPDF2.PdfReader(f)
                for page in reader.pages:
                    raw_text += (page.extract_text() or "") + "\n"

            title = os.path.basename(path)
            self.log_info(f"Ingested PDF: {path} ({_count_words(raw_text)} words)")
            return self._build_result("pdf", raw_text, title)
        except Exception as e:
            self.log_error(f"Failed to ingest PDF {path}: {e}")
            return self._empty_result("pdf")

    async def _ingest_docx(self, path: str) -> Dict[str, Any]:
        """Extract text from a DOCX file."""
        try:
            import docx

            doc = docx.Document(path)
            raw_text = "\n".join(para.text for para in doc.paragraphs)
            title = os.path.basename(path)
            self.log_info(f"Ingested DOCX: {path} ({_count_words(raw_text)} words)")
            return self._build_result("docx", raw_text, title)
        except Exception as e:
            self.log_error(f"Failed to ingest DOCX {path}: {e}")
            return self._empty_result("docx")

    async def _ingest_text(self, path: str) -> Dict[str, Any]:
        """Read a plain text or Markdown file."""
        try:
            with open(path, "r", encoding="utf-8") as f:
                raw_text = f.read()
            title = os.path.basename(path)
            self.log_info(
                f"Ingested text file: {path} ({_count_words(raw_text)} words)"
            )
            return self._build_result("text", raw_text, title)
        except Exception as e:
            self.log_error(f"Failed to ingest file {path}: {e}")
            return self._empty_result("text")

    def _build_result(
        self, source_type: str, raw_text: str, title: str
    ) -> Dict[str, Any]:
        return {
            "source_type": source_type,
            "raw_text": raw_text,
            "title": title,
            "word_count": _count_words(raw_text),
            "sections": _split_sections(raw_text),
        }

    def _empty_result(self, source_type: str) -> Dict[str, Any]:
        return {
            "source_type": source_type,
            "raw_text": "",
            "title": "",
            "word_count": 0,
            "sections": [],
        }
