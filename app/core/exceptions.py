from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse


def register_exception_handler(app: FastAPI):
    # Change "add_exception_handler" to "exception_handler"
    @app.exception_handler(Exception)
    async def unhandled_exception_handler(request: Request, exc: Exception):
        return JSONResponse(status_code=500, content={"detail": str(exc)})
