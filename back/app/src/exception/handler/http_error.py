from fastapi import HTTPException
from starlette.requests import Request
from starlette.responses import JSONResponse
from app.src.utils.response_builder import ResponseBuilder

async def http_error_handler(_: Request, exc: HTTPException) -> JSONResponse:
    response = ResponseBuilder()
    response.errors = [exc.detail]
    response.status = False
    return JSONResponse(response.to_dict(), status_code=exc.status_code)
