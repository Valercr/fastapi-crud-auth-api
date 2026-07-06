from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.core.database import Base, engine
from app.api.routes import auth, items


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(
    title="FastAPI CRUD Auth",
    lifespan=lifespan
)

app.include_router(auth.router)
app.include_router(items.router)

@app.get("/")
def root():
    return {"message": "API running"}