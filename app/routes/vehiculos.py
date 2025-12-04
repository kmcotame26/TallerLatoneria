from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from ..database import get_db
from .. import crud, schemas
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="app/templates")

router = APIRouter(prefix="/vehiculos", tags=["Vehículos"])

# RUTA HTML: esta debe ir antes del {vehiculo_id}
@router.get("/crear-form", response_class=HTMLResponse)
async def crear_form(request: Request):
    return templates.TemplateResponse(
        "vehiculos/crear.html",
        {"request": request}
    )

@router.get("/", response_model=list[schemas.VehiculoOut])
async def listar_vehiculos(db: AsyncSession = Depends(get_db)):
    return await crud.list_vehiculos(db)

@router.post("/", response_model=schemas.VehiculoOut, status_code=201)
async def crear_vehiculo(payload: schemas.VehiculoCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_vehiculo(db, payload)

# ESTA ES LA QUE CAUSABA PROBLEMAS
@router.get("/{vehiculo_id}", response_model=schemas.VehiculoOut)
async def obtener_vehiculo(vehiculo_id: int, db: AsyncSession = Depends(get_db)):
    obj = await crud.get_vehiculo(db, vehiculo_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Vehículo no encontrado")
    return obj

@router.put("/{vehiculo_id}", response_model=schemas.VehiculoOut)
async def actualizar_vehiculo(vehiculo_id: int, payload: schemas.VehiculoUpdate, db: AsyncSession = Depends(get_db)):
    obj = await crud.update_vehiculo(db, vehiculo_id, payload)
    if not obj:
        raise HTTPException(status_code=404, detail="Vehículo no encontrado")
    return obj

@router.delete("/{vehiculo_id}", response_model=schemas.VehiculoOut)
async def eliminar_vehiculo(vehiculo_id: int, db: AsyncSession = Depends(get_db)):
    obj = await crud.delete_vehiculo(db, vehiculo_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Vehículo no encontrado")
    return obj
