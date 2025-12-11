from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter(prefix="/embeddings", tags=["embeddings"])

class EmbeddingRequest(BaseModel):
    text: str

class EmbeddingResponse(BaseModel):
    vector: List[float]

@router.post("/", response_model=EmbeddingResponse)
async def embed(request: EmbeddingRequest):
    # Placeholder: fake vector so the API shape looks real
    fake_vector = [0.1, 0.2, 0.3]
    return EmbeddingResponse(vector=fake_vector)
