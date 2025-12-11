from fastapi import APIRouter, HTTPException, status

from app.models.schemas import ChatRequest, ChatResponse
from app.services.llm_client import llm_client

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(payload: ChatRequest):
    """
    Chat endpoint that forwards the user message to the LLM client
    and returns a generated reply.
    """
    if not payload.message.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Message must not be empty.",
        )

    reply = await llm_client.generate_reply(payload.message)
    return ChatResponse(reply=reply)
