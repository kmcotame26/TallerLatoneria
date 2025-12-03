from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from ..database import get_db
from .. import crud, schemas
from fastapi import UploadFile, File
import os


router = APIRouter(prefix="/vehiculos", tags=["Vehículos"])

@router.post("/", response_model=schemas.VehiculoOut, status_code=201)
async def crear_vehiculo(payload: schemas.VehiculoCreate, db: AsyncSession = Depends(get_db)):
    return await crud.create_vehiculo(db, payload)

@router.get("/", response_model=list[schemas.VehiculoOut])
async def listar_vehiculos(db: AsyncSession = Depends(get_db)):
    return await crud.list_vehiculos(db)

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

# Carpeta donde se guardarán las fotos
UPLOAD_DIR = "app/uploads/vehiculos"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/{vehiculo_id}/upload_foto")
async def upload_foto_vehiculo(
    vehiculo_id: int,
    file: UploadFile = File(...),
    db: AsyncSession = Depends(get_db)
):
    # Validar que el vehículo exista
    vehiculo = await crud.get_vehiculo(db, vehiculo_id)
    if not vehiculo:
        raise HTTPException(status_code=404, detail="Vehículo no encontrado")

    # Verificar tipo de archivo
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="El archivo debe ser una imagen")

    # Crear nombre del archivo
    extension = file.filename.split(".")[-1]
    filename = f"vehiculo_{vehiculo_id}.{extension}"
    file_path = os.path.join(UPLOAD_DIR, filename)

    # Guardar archivo en servidor
    with open(file_path, "wb") as f:
        f.write(await file.read())

    # URL pública
    file_url = f"/uploads/vehiculos/{filename}"

    return {
        "mensaje": "Foto subida correctamente",
        "vehiculo_id": vehiculo_id,
        "url_foto": file_url
    }
