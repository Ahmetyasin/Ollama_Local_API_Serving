from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
from typing import Optional
import os

app = FastAPI(title="Ollama API Wrapper")

# Get Ollama host and port from environment variables
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "localhost")
OLLAMA_PORT = os.getenv("OLLAMA_PORT", "11434")
OLLAMA_BASE_URL = f"http://{OLLAMA_HOST}:{OLLAMA_PORT}"

class GenerateRequest(BaseModel):
    model: str
    prompt: str
    stream: Optional[bool] = False

@app.get("/health")
async def health_check():
    return {"status": "healthy", "ollama_url": OLLAMA_BASE_URL}

@app.get("/models")
async def list_models():
    try:
        response = requests.get(f"{OLLAMA_BASE_URL}/api/tags")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Failed to connect to Ollama: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/generate")
async def generate(request: GenerateRequest):
    try:
        response = requests.post(
            f"{OLLAMA_BASE_URL}/api/generate",
            json={
                "model": request.model,
                "prompt": request.prompt,
                "stream": request.stream
            }
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Failed to connect to Ollama: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))