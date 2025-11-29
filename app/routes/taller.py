from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from ..database import get_db
from .. import crud, schemas

router = APIRouter(prefix="/taller", tags=["Taller"])

@router.post("/", response_model=schemas.TallerOut, status_code=201)
async def crear_taller(payload: schemas.TallerCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_taller(db, payload)

@router.get("/", response_model=list[schemas.TallerOut])
async def listar_taller(db: AsyncSession = Depends(get_db)):
    return await crud.list_taller(db)

@router.get("/{taller_id}", response_model=schemas.TallerOut)
async def obtener_taller(taller_id: int, db: AsyncSession = Depends(get_db)):
    obj = await crud.get_taller(db, taller_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Registro de taller no encontrado")
    return obj

@router.put("/{taller_id}", response_model=schemas.TallerOut)
async def actualizar_taller(taller_id: int, payload: schemas.TallerUpdate, db: AsyncSession = Depends(get_db)):
    obj = await crud.update_taller(db, taller_id, payload)
    if not obj:
        raise HTTPException(status_code=404, detail="Registro de taller no encontrado")
    return obj

@router.delete("/{taller_id}", response_model=schemas.TallerOut)
async def eliminar_taller(taller_id: int, db: AsyncSession = Depends(get_db)):
    obj = await crud.delete_taller(db, taller_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Registro de taller no encontrado")
    return obj
