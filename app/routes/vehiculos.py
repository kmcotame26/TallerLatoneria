from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="app/templates")

router = APIRouter()

# ---------- RUTA HTML ----------
@router.get("/listar", response_class=HTMLResponse)
async def listar_vehiculos_html(request: Request):
    return templates.TemplateResponse(
        "vehiculos/index.html",
        {"request": request}
    )

# ---------- RUTA API ----------
@router.get("/api/listar")
async def listar_vehiculos_api():
    return [
        {"id": 1, "marca": "Toyota"},
        {"id": 2, "marca": "Ford"}
    ]
