from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .models import Base
from .database import engine
from .routes import (
    usuarios,
    administradores,
    clientes,
    vehiculos,
    trabajos,
    facturas,
    taller as taller_routes,
)

app = FastAPI(title="API Taller de Latonería y Pintura")

app.mount("/uploads", StaticFiles(directory="app/uploads"), name="uploads")


app.include_router(usuarios.router)
app.include_router(administradores.router)
app.include_router(clientes.router)
app.include_router(vehiculos.router)
app.include_router(trabajos.router)
app.include_router(facturas.router)
app.include_router(taller_routes.router)

@app.get("/")
async def root():
    return {"mensaje": "API Taller funcionando"}

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.on_event("startup")
async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
