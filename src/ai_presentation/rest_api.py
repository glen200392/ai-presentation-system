"""REST API for AI Presentation System using FastAPI."""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import asyncio
from .orchestrator import PresentationOrchestrator

app = FastAPI(title="AI Presentation System", version="2.0.0")
orchestrator = PresentationOrchestrator()


class PresentationRequest(BaseModel):
    """Request model for presentation generation."""
    topic: str
    scenario: Optional[dict] = None
    content: Optional[dict] = None


class PresentationResponse(BaseModel):
    """Response model for presentation."""
    status: str
    message: str
    data: Optional[dict] = None


@app.get("/")
async def root():
    """Root endpoint."""
    return {"message": "AI Presentation System API"}


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}


@app.post("/generate", response_model=PresentationResponse)
async def generate_presentation(request: PresentationRequest):
    """Generate a presentation."""
    try:
        result = await orchestrator.generate_presentation({
            "topic": request.topic,
            "scenario": request.scenario or {},
            "content": request.content or {},
        })
        return PresentationResponse(
            status="success", message="Presentation generated", data=result
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/version")
async def get_version():
    """Get API version."""
    return {"version": "2.0.0"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
