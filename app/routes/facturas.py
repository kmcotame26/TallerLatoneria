from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from ..database import get_db
from .. import crud, schemas

router = APIRouter(prefix="/facturas", tags=["Facturas"])

@router.post("/", response_model=schemas.FacturaOut, status_code=201)
async def crear_factura(payload: schemas.FacturaCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_factura(db, payload)

@router.get("/", response_model=list[schemas.FacturaOut])
async def listar_facturas(db: AsyncSession = Depends(get_db)):
    return await crud.list_facturas(db)

@router.get("/{factura_id}", response_model=schemas.FacturaOut)
async def obtener_factura(factura_id: int, db: AsyncSession = Depends(get_db)):
    obj = await crud.get_factura(db, factura_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Factura no encontrada")
    return obj

@router.put("/{factura_id}", response_model=schemas.FacturaOut)
async def actualizar_factura(factura_id: int, payload: schemas.FacturaUpdate, db: AsyncSession = Depends(get_db)):
    obj = await crud.update_factura(db, factura_id, payload)
    if not obj:
        raise HTTPException(status_code=404, detail="Factura no encontrada")
    return obj

@router.delete("/{factura_id}", response_model=schemas.FacturaOut)
async def eliminar_factura(factura_id: int, db: AsyncSession = Depends(get_db)):
    obj = await crud.delete_factura(db, factura_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Factura no encontrada")
    return obj
