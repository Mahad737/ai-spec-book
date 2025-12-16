from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from rag import ingest_text, search

app = FastAPI(title="AI Book Chatbot")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "Backend running"}

class IngestRequest(BaseModel):
    text: str

class ChatRequest(BaseModel):
    question: str

@app.post("/ingest")
def ingest(req: IngestRequest):
    count = ingest_text(req.text)
    return {"chunks_added": count}

@app.post("/chat")
def chat(req: ChatRequest):
    answers = search(req.question)
    return {
        "answer": "\n\n".join(answers)
    }
