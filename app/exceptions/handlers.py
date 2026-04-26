from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse

from app.core.logger import get_logger
from app.exceptions.custom_exceptions import agentError

logger = get_logger(__name__)

async def global_exception_handler(request: Request, exc: Exception):
    logger.error(
        f"Unhandled error at {request.method} {request.url.path}",
        exc_info = True
    )

    return JSONResponse(
        status_code = 500,
        content = {"detail": "Internal Server Error"}
    )


async def http_exception_handler(request: Request, exc: HTTPException):
    logger.warning(f"HTTP error: {exc.detail}")

    return JSONResponse(
        status_code = exc.status_code,
        content = {"detail": exc.detail}
    )

async def agent_exception_handler(request: Request, exc: agentError):
    logger.warning(f"agent error: {exc.detail}")

    return JSONResponse(
        status_code = exc.status_code,
        content = {"detail": exc.detail}
    )

