from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from ..database import get_db
from .. import crud, schemas

router = APIRouter(prefix="/clientes", tags=["Clientes"])

@router.post("/", response_model=schemas.ClienteOut, status_code=201)
async def crear_cliente(payload: schemas.ClienteCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_cliente(db, payload)

@router.get("/", response_model=list[schemas.ClienteOut])
async def listar_clientes(db: AsyncSession = Depends(get_db)):
    return await crud.list_clientes(db)

@router.get("/{cliente_id}", response_model=schemas.ClienteOut)
async def obtener_cliente(cliente_id: int, db: AsyncSession = Depends(get_db)):
    obj = await crud.get_cliente(db, cliente_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return obj

@router.put("/{cliente_id}", response_model=schemas.ClienteOut)
async def actualizar_cliente(cliente_id: int, payload: schemas.ClienteUpdate, db: AsyncSession = Depends(get_db)):
    obj = await crud.update_cliente(db, cliente_id, payload)
    if not obj:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return obj

@router.delete("/{cliente_id}", response_model=schemas.ClienteOut)
async def eliminar_cliente(cliente_id: int, db: AsyncSession = Depends(get_db)):
    obj = await crud.delete_cliente(db, cliente_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return obj
