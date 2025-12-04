from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

from starlette.requests import Request
from fastapi.responses import HTMLResponse

# Routers
from app.routes import vehiculos, clientes, usuarios, administradores, facturas, trabajos

app = FastAPI()

# STATIC para Render
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# templates Jinja2
templates = Jinja2Templates(directory="app/templates")


# ---------- RUTAS DE INICIO ----------
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# ---------- INCLUIR ROUTERS ----------
app.include_router(vehiculos.router, prefix="/vehiculos")
app.include_router(clientes.router, prefix="/clientes")
app.include_router(usuarios.router, prefix="/usuarios")
app.include_router(administradores.router, prefix="/administradores")
app.include_router(facturas.router, prefix="/facturas")
app.include_router(trabajos.router, prefix="/trabajos")
