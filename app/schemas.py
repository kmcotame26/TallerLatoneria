# app/schemas.py
from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date

# ===== USUARIOS =====
class UsuarioBase(BaseModel):
    nombre: str
    correo: EmailStr
    rol: str = "empleado"
    activo: bool = True

class UsuarioCreate(UsuarioBase):
    pass

class UsuarioUpdate(BaseModel):
    nombre: Optional[str] = None
    correo: Optional[EmailStr] = None
    rol: Optional[str] = None
    activo: Optional[bool] = None

class UsuarioOut(UsuarioBase):
    id_usuario: int
    class Config:
        from_attributes = True


# ===== ADMINISTRADORES =====
class AdministradorBase(BaseModel):
    nombre: str
    correo: EmailStr
    telefono: Optional[str] = None
    cargo: Optional[str] = None

class AdministradorCreate(AdministradorBase):
    pass

class AdministradorUpdate(BaseModel):
    nombre: Optional[str] = None
    correo: Optional[EmailStr] = None
    telefono: Optional[str] = None
    cargo: Optional[str] = None

class AdministradorOut(AdministradorBase):
    id_admin: int
    class Config:
        from_attributes = True


# ===== CLIENTES =====
class ClienteBase(BaseModel):
    nombre: str
    correo: Optional[EmailStr] = None
    telefono: Optional[str] = None
    direccion: Optional[str] = None

class ClienteCreate(ClienteBase):
    pass

class ClienteUpdate(BaseModel):
    nombre: Optional[str] = None
    correo: Optional[EmailStr] = None
    telefono: Optional[str] = None
    direccion: Optional[str] = None

class ClienteOut(ClienteBase):
    id_cliente: int
    class Config:
        from_attributes = True


# ===== VEHÍCULOS =====
class VehiculoBase(BaseModel):
    cliente_id: int
    placa: str
    marca: str
    modelo: Optional[str] = None
    anio: Optional[int] = None
    color: Optional[str] = None

class VehiculoCreate(VehiculoBase):
    pass

class VehiculoUpdate(BaseModel):
    cliente_id: Optional[int] = None
    placa: Optional[str] = None
    marca: Optional[str] = None
    modelo: Optional[str] = None
    anio: Optional[int] = None
    color: Optional[str] = None

class VehiculoOut(VehiculoBase):
    id_vehiculo: int
    class Config:
        from_attributes = True


# ===== TRABAJOS =====
class TrabajoBase(BaseModel):
    vehiculo_id: int
    descripcion: str
    lado: Optional[str] = None
    sub_costo: float
    fecha_inicio: Optional[date] = None
    fecha_fin: Optional[date] = None
    estado: str = "en_proceso"

class TrabajoCreate(TrabajoBase):
    pass

class TrabajoUpdate(BaseModel):
    vehiculo_id: Optional[int] = None
    descripcion: Optional[str] = None
    lado: Optional[str] = None
    sub_costo: Optional[float] = None
    fecha_inicio: Optional[date] = None
    fecha_fin: Optional[date] = None
    estado: Optional[str] = None

class TrabajoOut(TrabajoBase):
    id_trabajo: int
    class Config:
        from_attributes = True


# ===== TALLER =====
class TallerBase(BaseModel):
    trabajo_id: int
    estado_reparacion: str = "en_arreglo"
    observaciones: Optional[str] = None
    bahia: Optional[str] = None

class TallerCreate(TallerBase):
    pass

class TallerUpdate(BaseModel):
    trabajo_id: Optional[int] = None
    estado_reparacion: Optional[str] = None
    observaciones: Optional[str] = None
    bahia: Optional[str] = None

class TallerOut(TallerBase):
    id_taller: int
    class Config:
        from_attributes = True


# ===== FACTURAS =====
class FacturaBase(BaseModel):
    cliente_id: Optional[int] = None
    trabajo_id: Optional[int] = None
    fecha_emision: Optional[date] = None
    subtotal: float
    impuestos: float
    total: float
    pagada: bool = False

class FacturaCreate(FacturaBase):
    pass

class FacturaUpdate(BaseModel):
    cliente_id: Optional[int] = None
    trabajo_id: Optional[int] = None
    fecha_emision: Optional[date] = None
    subtotal: Optional[float] = None
    impuestos: Optional[float] = None
    total: Optional[float] = None
    pagada: Optional[bool] = None

class FacturaOut(FacturaBase):
    id_factura: int
    class Config:
        from_attributes = True
