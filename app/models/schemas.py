from pydantic import BaseModel, Field
from typing import List


class ChatRequest(BaseModel):
    message: str = Field(..., description="User input message to the assistant.")


class ChatResponse(BaseModel):
    reply: str = Field(..., description="Assistant response message.")


class EmbeddingRequest(BaseModel):
    text: str = Field(..., description="Input text to convert into an embedding vector.")


class EmbeddingResponse(BaseModel):
    embedding: List[float] = Field(
        ..., description="Numerical embedding representation of the input text."
    )
