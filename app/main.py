from typing import Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from app.core.config import settings
from app.agent.agent import run_agent
from app.core.logger import get_logger, setup_logger
from app.exceptions.custom_exceptions import agentError
from app.exceptions.handlers import (
    agent_exception_handler,
    global_exception_handler,
    http_exception_handler,
)
from app.schemas.ask import AskRequest, AskResponse

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
# API
# -------------------------

@app.post("/ask", response_model=AskResponse)
def ask(request: AskRequest) -> AskResponse:
    """
    Handle user query via AI agent.

    Args:
        request (AskRequest): User input query.

    Returns:
        AskResponse: Structured response containing answer or error.
    """
    logger.info(f"Received query: {request.query}")
    result = run_agent(request.query)
    logger.info(f"Agent result: {result}")
    return AskResponse(
        query=request.query,
        answer=result,
        error=None
    )