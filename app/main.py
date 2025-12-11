from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import chat, embeddings

app = FastAPI(
    title="LLM Microservice Hub",
    description="Production-style FastAPI + AsyncIO microservice for LLM chat and embeddings.",
    version="0.1.0",
)

# Allow local / frontend tools to call this API (optional but realistic)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check
@app.get("/health", tags=["health"])
async def health_check():
    return {"status": "ok"}


# Mount API routers
app.include_router(chat.router, prefix="/api", tags=["chat"])
app.include_router(embeddings.router, prefix="/api", tags=["embeddings"])
