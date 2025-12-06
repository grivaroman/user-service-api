from fastapi import FastAPI
from app.api import auth, users
from app.core.config import settings

app = FastAPI(title="User Service API")

app.include_router(auth.router, prefix="/api")
app.include_router(users.router, prefix="/api")

@app.get("/")
async def root():
    return {"status": "ok", "service": "user-service"}
