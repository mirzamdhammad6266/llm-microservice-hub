from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/chat", tags=["chat"])

class ChatRequest(BaseModel):
    prompt: str

class ChatResponse(BaseModel):
    answer: str

@router.post("/", response_model=ChatResponse)
async def chat(request: ChatRequest):
    # For now, return a simple placeholder response
    return ChatResponse(answer=f"Placeholder LLM response for: {request.prompt}")
