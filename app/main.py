from app.core.config import GOOGLE_API_KEY
from fastapi import FastAPI
from app.schemas.ask import AskRequest
from app.agent.agent import run_agent

app = FastAPI()

@app.post("/ask")
def ask(request: AskRequest):
    result = run_agent(request.query)
    return {"answer": result}
