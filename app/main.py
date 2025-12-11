from fastapi import FastAPI

app = FastAPI(title="LLM Microservice Hub")

@app.get("/health")
async def health_check():
    return {"status": "ok", "service": "llm-microservice-hub"}

@app.get("/")
async def root():
    return {"message": "LLM Microservice Hub is running"}
