from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from app.agent.agent import run_agent
from app.core.config import settings
from app.core.logger import get_logger, setup_logger
from app.exceptions.custom_exceptions import agentError
from app.exceptions.handlers import global_exception_handler, http_exception_handler, agent_exception_handler
from app.schemas.ask import AskRequest

# -------------------------
# Setup
# -------------------------

setup_logger(log_level = settings.LOG_LEVEL, log_path = settings.LOG_DIR)

logger = get_logger(__name__)

app = FastAPI()

app.add_exception_handler(exc_class_or_status_code = Exception, handler = global_exception_handler)
app.add_exception_handler(exc_class_or_status_code = HTTPException, handler = http_exception_handler)
app.add_exception_handler(exc_class_or_status_code = agentError, handler = agent_exception_handler)


# -------------------------
# Request Model
# -------------------------

class QueryRequest(BaseModel):
    query: str = Field(min_length = 1)

# -------------------------
# API
# -------------------------

@app.post("/ask")
def ask(request: AskRequest):
    logger.info(f"Received query: {request.query}")
    result = run_agent(request.query)
    return {"answer": result}
