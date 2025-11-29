from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from ..database import get_db
from .. import crud, schemas

router = APIRouter(prefix="/administradores", tags=["Administradores"])

@router.post("/", response_model=schemas.AdministradorOut, status_code=201)
async def crear_administrador(payload: schemas.AdministradorCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_administrador(db, payload)

@router.get("/", response_model=list[schemas.AdministradorOut])
async def listar_administradores(db: AsyncSession = Depends(get_db)):
    return await crud.list_administradores(db)

@router.get("/{admin_id}", response_model=schemas.AdministradorOut)
async def obtener_administrador(admin_id: int, db: AsyncSession = Depends(get_db)):
    obj = await crud.get_administrador(db, admin_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Administrador no encontrado")
    return obj

@router.put("/{admin_id}", response_model=schemas.AdministradorOut)
async def actualizar_administrador(admin_id: int, payload: schemas.AdministradorUpdate, db: AsyncSession = Depends(get_db)):
    obj = await crud.update_administrador(db, admin_id, payload)
    if not obj:
        raise HTTPException(status_code=404, detail="Administrador no encontrado")
    return obj

@router.delete("/{admin_id}", response_model=schemas.AdministradorOut)
async def eliminar_administrador(admin_id: int, db: AsyncSession = Depends(get_db)):
    obj = await crud.delete_administrador(db, admin_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Administrador no encontrado")
    return obj
