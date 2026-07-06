from fastapi import FastAPI

from app.core.database import Base, engine
from app.api.routes import auth, items

# Crear app
app = FastAPI(title="FastAPI CRUD Auth")

# Crear tablas en DB (solo para desarrollo)
Base.metadata.create_all(bind=engine)

# Registrar rutas
app.include_router(auth.router)
app.include_router(items.router)


@app.get("/")
def root():
    return {"message": "API running"}