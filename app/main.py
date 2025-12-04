# app/main.py
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
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
app = FastAPI()

templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/vehiculos/crear")
async def vehiculo_form(request: Request):
    return templates.TemplateResponse("vehiculos/crear.html", {"request": request})

@app.get("/vehiculos/listar")
async def vehiculos_listado(request: Request):
    return templates.TemplateResponse("vehiculos/listar.html", {"request": request})


# Routers API
app.include_router(usuarios.router)
app.include_router(administradores.router)
app.include_router(clientes.router)
app.include_router(vehiculos.router)
app.include_router(trabajos.router)
app.include_router(facturas.router)
app.include_router(taller_routes.router)

# Health
@app.get("/health")
async def health():
    return {"status": "ok"}

# Crear tablas
@app.on_event("startup")
async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
