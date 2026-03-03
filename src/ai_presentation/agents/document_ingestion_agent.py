"""Document Ingestion Agent for parsing PDFs, DOCX, plain text, and URLs."""

import logging
import os
from typing import Any, Dict, List

from .base_agent import BaseAgent

logger = logging.getLogger(__name__)


class DocumentIngestionAgent(BaseAgent):
    """Parses various document formats into structured content."""

    def __init__(self, config: Dict[str, Any] = None):
        """Initialize DocumentIngestionAgent."""
        super().__init__("DocumentIngestion", config or {})
        logger.info("DocumentIngestionAgent initialized")

    def process(self, *args, **kwargs):
        """Process a document source."""
        return self.ingest(*args, **kwargs)

    async def ingest(self, source: str) -> Dict[str, Any]:
        """Ingest content from a file path or URL.

        Args:
            source: File path (PDF/DOCX/TXT/MD) or HTTP(S) URL.

        Returns:
            Structured dict with source_type, raw_text, title, word_count, sections.
        """
        logger.info(f"Ingesting source: {source}")
        if source.startswith("http://") or source.startswith("https://"):
            return await self._ingest_url(source)

        ext = os.path.splitext(source)[1].lower()
        if ext == ".pdf":
            return await self._ingest_pdf(source)
        if ext in (".docx", ".doc"):
            return await self._ingest_docx(source)
        # Plain text / Markdown
        return await self._ingest_text(source)

    async def _ingest_pdf(self, path: str) -> Dict[str, Any]:
        """Extract text from a PDF file using PyPDF2."""
        try:
            import PyPDF2  # noqa: PLC0415
        except ImportError as exc:
            raise ImportError("PyPDF2 is required for PDF ingestion: pip install PyPDF2>=3.0.0") from exc

        pages: List[str] = []
        with open(path, "rb") as fh:
            reader = PyPDF2.PdfReader(fh)
            for page in reader.pages:
                text = page.extract_text() or ""
                pages.append(text)

        raw_text = "\n".join(pages)
        return self._build_result("pdf", raw_text, os.path.basename(path))

    async def _ingest_docx(self, path: str) -> Dict[str, Any]:
        """Extract text from a DOCX file using python-docx."""
        try:
            import docx  # noqa: PLC0415
        except ImportError as exc:
            raise ImportError(
                "python-docx is required for DOCX ingestion: pip install python-docx>=0.8.11"
            ) from exc

        doc = docx.Document(path)
        paragraphs = [p.text for p in doc.paragraphs if p.text.strip()]
        raw_text = "\n".join(paragraphs)
        title = paragraphs[0] if paragraphs else os.path.basename(path)
        return self._build_result("docx", raw_text, title)

    async def _ingest_text(self, path: str) -> Dict[str, Any]:
        """Read a plain-text or Markdown file."""
        with open(path, "r", encoding="utf-8") as fh:
            raw_text = fh.read()
        lines = raw_text.splitlines()
        title = lines[0].lstrip("# ").strip() if lines else os.path.basename(path)
        source_type = "markdown" if path.endswith((".md", ".markdown")) else "text"
        return self._build_result(source_type, raw_text, title)

    async def _ingest_url(self, url: str) -> Dict[str, Any]:
        """Fetch and extract main body text from a URL."""
        try:
            import requests  # noqa: PLC0415
            from bs4 import BeautifulSoup  # noqa: PLC0415
        except ImportError as exc:
            raise ImportError(
                "requests and beautifulsoup4 are required for URL ingestion: "
                "pip install requests beautifulsoup4 lxml"
            ) from exc

        response = requests.get(url, timeout=30)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "lxml")

        # Remove script and style elements
        for tag in soup(["script", "style", "nav", "footer", "header"]):
            tag.decompose()

        title_tag = soup.find("title")
        title = title_tag.get_text(strip=True) if title_tag else url

        main = soup.find("main") or soup.find("article") or soup.find("body")
        raw_text = main.get_text(separator="\n", strip=True) if main else soup.get_text(separator="\n", strip=True)

        return self._build_result("url", raw_text, title)

    def _build_result(self, source_type: str, raw_text: str, title: str) -> Dict[str, Any]:
        """Build the structured result dict."""
        words = raw_text.split()
        lines = [ln.strip() for ln in raw_text.splitlines() if ln.strip()]
        sections = self._detect_sections(lines)
        return {
            "source_type": source_type,
            "raw_text": raw_text,
            "title": title,
            "word_count": len(words),
            "sections": sections,
        }

    def _detect_sections(self, lines: List[str]) -> List[Dict[str, str]]:
        """Heuristically detect sections from text lines."""
        sections: List[Dict[str, str]] = []
        current: List[str] = []
        current_heading = "Introduction"

        for line in lines:
            # Simple heuristic: short lines that look like headings
            if len(line) < 80 and line.endswith((":", "?", "!")) or (
                line.isupper() and len(line.split()) <= 8
            ):
                if current:
                    sections.append({"heading": current_heading, "content": " ".join(current)})
                    current = []
                current_heading = line.rstrip(":")
            else:
                current.append(line)

        if current:
            sections.append({"heading": current_heading, "content": " ".join(current)})

        return sections or [{"heading": "Content", "content": " ".join(lines[:50])}]

    async def execute(self, input_data: Dict[str, Any] = None) -> Dict[str, Any]:
        """Execute the agent task."""
        return {"status": "ready", "agent": "DocumentIngestion"}
