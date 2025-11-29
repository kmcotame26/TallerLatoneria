from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from ..database import get_db
from .. import crud, schemas

router = APIRouter(prefix="/trabajos", tags=["Trabajos"])

@router.post("/", response_model=schemas.TrabajoOut, status_code=201)
async def crear_trabajo(payload: schemas.TrabajoCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_trabajo(db, payload)

@router.get("/", response_model=list[schemas.TrabajoOut])
async def listar_trabajos(db: AsyncSession = Depends(get_db)):
    return await crud.list_trabajos(db)

@router.get("/{trabajo_id}", response_model=schemas.TrabajoOut)
async def obtener_trabajo(trabajo_id: int, db: AsyncSession = Depends(get_db)):
    obj = await crud.get_trabajo(db, trabajo_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Trabajo no encontrado")
    return obj

@router.put("/{trabajo_id}", response_model=schemas.TrabajoOut)
async def actualizar_trabajo(trabajo_id: int, payload: schemas.TrabajoUpdate, db: AsyncSession = Depends(get_db)):
    obj = await crud.update_trabajo(db, trabajo_id, payload)
    if not obj:
        raise HTTPException(status_code=404, detail="Trabajo no encontrado")
    return obj

@router.delete("/{trabajo_id}", response_model=schemas.TrabajoOut)
async def eliminar_trabajo(trabajo_id: int, db: AsyncSession = Depends(get_db)):
    obj = await crud.delete_trabajo(db, trabajo_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Trabajo no encontrado")
    return obj
