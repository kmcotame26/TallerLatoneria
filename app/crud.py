# app/crud.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from . import models, schemas

# ===== USUARIOS =====
async def create_usuario(db: AsyncSession, data: schemas.UsuarioCreate):
    obj = models.Usuario(
        nombre=data.nombre,
        correo=data.correo,
        rol=data.rol,
        activo=data.activo,
    )
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj

async def list_usuarios(db: AsyncSession):
    res = await db.execute(select(models.Usuario))
    return res.scalars().all()

async def get_usuario(db: AsyncSession, usuario_id: int):
    return await db.get(models.Usuario, usuario_id)

async def update_usuario(db: AsyncSession, usuario_id: int, data: schemas.UsuarioUpdate):
    obj = await db.get(models.Usuario, usuario_id)
    if not obj:
        return None
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(obj, field, value)
    await db.commit()
    await db.refresh(obj)
    return obj

async def delete_usuario(db: AsyncSession, usuario_id: int):
    obj = await db.get(models.Usuario, usuario_id)
    if not obj:
        return None
    await db.delete(obj)
    await db.commit()
    return obj


# ===== ADMINISTRADORES =====
async def create_administrador(db: AsyncSession, data: schemas.AdministradorCreate):
    obj = models.Administrador(
        nombre=data.nombre,
        correo=data.correo,
        telefono=data.telefono,
        cargo=data.cargo,
    )
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj

async def list_administradores(db: AsyncSession):
    res = await db.execute(select(models.Administrador))
    return res.scalars().all()

async def get_administrador(db: AsyncSession, admin_id: int):
    return await db.get(models.Administrador, admin_id)

async def update_administrador(db: AsyncSession, admin_id: int, data: schemas.AdministradorUpdate):
    obj = await db.get(models.Administrador, admin_id)
    if not obj:
        return None
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(obj, field, value)
    await db.commit()
    await db.refresh(obj)
    return obj

async def delete_administrador(db: AsyncSession, admin_id: int):
    obj = await db.get(models.Administrador, admin_id)
    if not obj:
        return None
    await db.delete(obj)
    await db.commit()
    return obj


# ===== CLIENTES =====
async def create_cliente(db: AsyncSession, data: schemas.ClienteCreate):
    obj = models.Cliente(
        nombre=data.nombre,
        correo=data.correo,
        telefono=data.telefono,
        direccion=data.direccion,
    )
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj

async def list_clientes(db: AsyncSession):
    res = await db.execute(select(models.Cliente))
    return res.scalars().all()

async def get_cliente(db: AsyncSession, cliente_id: int):
    return await db.get(models.Cliente, cliente_id)

async def update_cliente(db: AsyncSession, cliente_id: int, data: schemas.ClienteUpdate):
    obj = await db.get(models.Cliente, cliente_id)
    if not obj:
        return None
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(obj, field, value)
    await db.commit()
    await db.refresh(obj)
    return obj

async def delete_cliente(db: AsyncSession, cliente_id: int):
    obj = await db.get(models.Cliente, cliente_id)
    if not obj:
        return None
    await db.delete(obj)
    await db.commit()
    return obj


# ===== VEHÍCULOS =====
async def create_vehiculo(db: AsyncSession, data: schemas.VehiculoCreate):
    obj = models.Vehiculo(
        cliente_id=data.cliente_id,
        placa=data.placa,
        marca=data.marca,
        modelo=data.modelo,
        anio=data.anio,
        color=data.color,
    )
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj

async def list_vehiculos(db: AsyncSession):
    res = await db.execute(select(models.Vehiculo))
    return res.scalars().all()

async def get_vehiculo(db: AsyncSession, vehiculo_id: int):
    return await db.get(models.Vehiculo, vehiculo_id)

async def update_vehiculo(db: AsyncSession, vehiculo_id: int, data: schemas.VehiculoUpdate):
    obj = await db.get(models.Vehiculo, vehiculo_id)
    if not obj:
        return None
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(obj, field, value)
    await db.commit()
    await db.refresh(obj)
    return obj

async def delete_vehiculo(db: AsyncSession, vehiculo_id: int):
    obj = await db.get(models.Vehiculo, vehiculo_id)
    if not obj:
        return None
    await db.delete(obj)
    await db.commit()
    return obj


# ===== TRABAJOS =====
async def create_trabajo(db: AsyncSession, data: schemas.TrabajoCreate):
    obj = models.Trabajo(
        vehiculo_id=data.vehiculo_id,
        descripcion=data.descripcion,
        lado=data.lado,
        sub_costo=data.sub_costo,
        fecha_inicio=data.fecha_inicio,
        fecha_fin=data.fecha_fin,
        estado=data.estado,
    )
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj

async def list_trabajos(db: AsyncSession):
    res = await db.execute(select(models.Trabajo))
    return res.scalars().all()

async def get_trabajo(db: AsyncSession, trabajo_id: int):
    return await db.get(models.Trabajo, trabajo_id)

async def update_trabajo(db: AsyncSession, trabajo_id: int, data: schemas.TrabajoUpdate):
    obj = await db.get(models.Trabajo, trabajo_id)
    if not obj:
        return None
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(obj, field, value)
    await db.commit()
    await db.refresh(obj)
    return obj

async def delete_trabajo(db: AsyncSession, trabajo_id: int):
    obj = await db.get(models.Trabajo, trabajo_id)
    if not obj:
        return None
    await db.delete(obj)
    await db.commit()
    return obj


# ===== TALLER =====
async def create_taller(db: AsyncSession, data: schemas.TallerCreate):
    obj = models.Taller(
        trabajo_id=data.trabajo_id,
        estado_reparacion=data.estado_reparacion,
        observaciones=data.observaciones,
        bahia=data.bahia,
    )
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj

async def list_taller(db: AsyncSession):
    res = await db.execute(select(models.Taller))
    return res.scalars().all()

async def get_taller(db: AsyncSession, taller_id: int):
    return await db.get(models.Taller, taller_id)

async def update_taller(db: AsyncSession, taller_id: int, data: schemas.TallerUpdate):
    obj = await db.get(models.Taller, taller_id)
    if not obj:
        return None
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(obj, field, value)
    await db.commit()
    await db.refresh(obj)
    return obj

async def delete_taller(db: AsyncSession, taller_id: int):
    obj = await db.get(models.Taller, taller_id)
    if not obj:
        return None
    await db.delete(obj)
    await db.commit()
    return obj


# ===== FACTURAS =====
async def create_factura(db: AsyncSession, data: schemas.FacturaCreate):
    obj = models.Factura(
        cliente_id=data.cliente_id,
        trabajo_id=data.trabajo_id,
        fecha_emision=data.fecha_emision,
        subtotal=data.subtotal,
        impuestos=data.impuestos,
        total=data.total,
        pagada=data.pagada,
    )
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj

async def list_facturas(db: AsyncSession):
    res = await db.execute(select(models.Factura))
    return res.scalars().all()

async def get_factura(db: AsyncSession, factura_id: int):
    return await db.get(models.Factura, factura_id)

async def update_factura(db: AsyncSession, factura_id: int, data: schemas.FacturaUpdate):
    obj = await db.get(models.Factura, factura_id)
    if not obj:
        return None
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(obj, field, value)
    await db.commit()
    await db.refresh(obj)
    return obj

async def delete_factura(db: AsyncSession, factura_id: int):
    obj = await db.get(models.Factura, factura_id)
    if not obj:
        return None
    await db.delete(obj)
    await db.commit()
    return obj
