from sqlalchemy import Column, Integer, String,Float,Date, ForeignKey 
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

# llamado a la base para crear tablas
Base = declarative_base()

# DEFINICION DE LAS TABLAS DE MI MODELO

# Usuario
class Usuario(Base):
    __tablename__='usuarios'
    id = Column(Integer, primary_key = True, autoincrement = True)
    nombres = Column(String(50))
    edad = Column(Integer)
    telefono = Column(String(12))
    correo = Column(String(20))
    contraseña = Column(String(20))
    fechaRegistro = Column(Date)
    ciudad = Column(String(50))
    metaAhorro = Column(Float)

class Gasto(Base):
    __tablename__='gastos'
    id = Column(Integer, autoincrement = True)
    descripcionGasto = Column(String(200))
    valorGastado = Column(Integer)
    fechaGasto = Column(Date)

class Categoria(Base):
    __tablename__='categorias'
    id = Column(Integer, autoincrement = True)
    nombre = Column(String(50))
    descripcionCategoria = Column(String(200))
    imagenRuta = Column(String(255))

class Ingreso(Base):
    __tablename__='ingresos'
    id = Column(Integer, autoincrement = True)
    valorIngreso = Column(Integer)
    descripcionIngreso = Column(String(200))
    fechaIngreso = Column(Date)