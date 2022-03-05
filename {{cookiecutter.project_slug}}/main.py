# Local imports
import os
import json

# Server Runner
import uvicorn
import nest_asyncio

# FastAPI
from fastapi import FastAPI

from fastapi import Request
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.responses import ORJSONResponse
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from fastapi.openapi.utils import get_openapi

# Slowapi/RatelImiter
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware

# Limiter
from limiter import limiter as limiter_func

app = FastAPI(
    docs_url="{{cookiecutter.playground_endpoint}}",
    redoc_url="{{cookiecutter.docs_endpoint}}"
    )

limiter = limiter_func()
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.add_middleware(SlowAPIMiddleware)

dir_path = os.path.dirname(os.path.realpath(__file__))

@app.get("/")
async def root():
    return {"message": "Hello World"}

# Run API
if __name__ == '__main__':
	uvicorn.run(
        "main:app",
        host='{{cookiecutter.base}}',
        port={{cookiecutter.port}},
        reload=True,
        debug=True, 
        workers={{cookiecutter.workers}}
        )