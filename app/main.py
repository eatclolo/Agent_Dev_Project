from app.core.config import settings

from fastapi import FastAPI, HTTPException

from app.core.logger import setup_logger, get_logger
from app.exceptions.handlers import global_exception_handler, http_exception_handler
from app.schemas.ask import AskRequest
from app.agent.agent import run_agent

# -------------------------
# Setup
# -------------------------

setup_logger(log_level = settings.LOG_LEVEL, log_path = settings.LOG_DIR)

logger = get_logger(__name__)

app = FastAPI()

app.add_exception_handler(exc_class_or_status_code = Exception, handler = global_exception_handler)
app.add_exception_handler(exc_class_or_status_code = HTTPException, handler = http_exception_handler)


@app.post("/ask")
def ask(request: AskRequest):
    result = run_agent(request.query)
    return {"answer": result}
