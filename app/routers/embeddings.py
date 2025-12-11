from fastapi import APIRouter, HTTPException, status

from app.models.schemas import EmbeddingRequest, EmbeddingResponse
from app.services.llm_client import llm_client

router = APIRouter()


@router.post("/embeddings", response_model=EmbeddingResponse)
async def embeddings_endpoint(payload: EmbeddingRequest):
    """
    Embeddings endpoint that converts input text into a vector representation.
    """
    if not payload.text.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Text must not be empty.",
        )

    embedding = await llm_client.generate_embedding(payload.text)
    return EmbeddingResponse(embedding=embedding)
