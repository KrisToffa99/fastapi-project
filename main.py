from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from api.router import api_router
from core.config import settings

app = FastAPI(title="Book API",
              description="A simple API for managing books",
              version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=settings.API_PREFIX)

@app.get("/")
async def root():
    """Redirect root to docs"""
    return RedirectResponse(url="/docs")

@app.get("/healthcheck")
async def health_check():
    """Checks if server is active."""
    return {"status": "active"}