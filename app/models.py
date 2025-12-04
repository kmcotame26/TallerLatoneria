# app/models.py
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Float, Date, Boolean, ForeignKey, Numeric

class Base(DeclarativeBase):
    pass


# ===== USUARIOS (usuarios generales del sistema) =====
class Usuario(Base):
    __tablename__ = "usuarios"

    id_usuario: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False)
    correo: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    rol: Mapped[str] = mapped_column(String(20), nullable=False, default="empleado")
    activo: Mapped[bool] = mapped_column(Boolean, default=True)


# ===== ADMINISTRADORES (admins del taller) =====
class Administrador(Base):
    __tablename__ = "administradores"

    id_admin: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False)
    correo: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    telefono: Mapped[str | None] = mapped_column(String(20), nullable=True)
    cargo: Mapped[str | None] = mapped_column(String(100), nullable=True)


# ===== CLIENTES =====
class Cliente(Base):
    __tablename__ = "clientes"

    id_cliente: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False)
    correo: Mapped[str | None] = mapped_column(String(255), nullable=True)
    telefono: Mapped[str | None] = mapped_column(String(20), nullable=True)
    direccion: Mapped[str | None] = mapped_column(String(255), nullable=True)

    vehiculos = relationship("Vehiculo", back_populates="cliente", cascade="all, delete-orphan")
    facturas = relationship("Factura", back_populates="cliente", cascade="all, delete-orphan")


class Vehiculo(Base):
    __tablename__ = "vehiculos"

    id_vehiculo: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    cliente_id: Mapped[int] = mapped_column(ForeignKey("clientes.id_cliente", ondelete="CASCADE"))
    placa: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    marca: Mapped[str] = mapped_column(String(50), nullable=False)
    modelo: Mapped[str | None] = mapped_column(String(50), nullable=True)
    anio: Mapped[int | None] = mapped_column(Integer, nullable=True)
    color: Mapped[str | None] = mapped_column(String(30), nullable=True)

    cliente = relationship("Cliente", back_populates="vehiculos")
    trabajos = relationship("Trabajo", back_populates="vehiculo", cascade="all, delete-orphan")


# ===== TRABAJOS (lado, sub_costo, fecha_fin, etc.) =====
class Trabajo(Base):
    __tablename__ = "trabajos"

    id_trabajo: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    vehiculo_id: Mapped[int] = mapped_column(ForeignKey("vehiculos.id_vehiculo", ondelete="CASCADE"))
    descripcion: Mapped[str] = mapped_column(String(255), nullable=False)
    lado: Mapped[str | None] = mapped_column(String(50), nullable=True)  # ejemplo: "lado derecho", "frontal"
    sub_costo: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False, default=0)
    fecha_inicio: Mapped[Date | None] = mapped_column(Date, nullable=True)
    fecha_fin: Mapped[Date | None] = mapped_column(Date, nullable=True)
    estado: Mapped[str] = mapped_column(String(50), nullable=False, default="en_proceso")  # en_proceso, finalizado

    vehiculo = relationship("Vehiculo", back_populates="trabajos")
    taller = relationship("Taller", back_populates="trabajo", uselist=False)
    factura = relationship("Factura", back_populates="trabajo", uselist=False)


# ===== TALLER (estado de reparaciones) =====
class Taller(Base):
    __tablename__ = "taller"

    id_taller: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    trabajo_id: Mapped[int] = mapped_column(ForeignKey("trabajos.id_trabajo", ondelete="CASCADE"), unique=True)
    estado_reparacion: Mapped[str] = mapped_column(String(50), nullable=False, default="en_arreglo")
    observaciones: Mapped[str | None] = mapped_column(String(255), nullable=True)
    bahia: Mapped[str | None] = mapped_column(String(50), nullable=True)

    trabajo = relationship("Trabajo", back_populates="taller")


# ===== FACTURAS =====
class Factura(Base):
    __tablename__ = "facturas"

    id_factura: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    cliente_id: Mapped[int | None] = mapped_column(ForeignKey("clientes.id_cliente", ondelete="SET NULL"))
    trabajo_id: Mapped[int | None] = mapped_column(ForeignKey("trabajos.id_trabajo", ondelete="SET NULL"))
    fecha_emision: Mapped[Date | None] = mapped_column(Date, nullable=True)
    subtotal: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False, default=0)
    impuestos: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False, default=0)
    total: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False, default=0)
    pagada: Mapped[bool] = mapped_column(Boolean, default=False)

    cliente = relationship("Cliente", back_populates="facturas")
    trabajo = relationship("Trabajo", back_populates="factura")
