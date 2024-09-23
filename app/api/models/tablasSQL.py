from sqlalchemy import Column, Integer, String,Float,Date, ForeignKey 
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

# llamado a la base para crear tablas
Base = declarative_base()

# DEFINICION DE LAS TABLAS DE MI MODELO

# Usuario
class Usuario(Base):
    __tablename__='usuarios'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombres = Column(String(50))
    fechaNacimiento = Column(Date)
    ubicacion = Column(String(100))
    metaAhorro = Column(Float)

class Gasto(Base):
    __tablename__='gastos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    descripcionGasto = Column(String(200))
    valorGastado = Column(Integer)
    fechaGasto = Column(Date)

class Categoria(Base):
    __tablename__='categorias'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50))
    descripcionCategoria = Column(String(200))
    imagenRuta = Column(String(255))
    pass

class Ingreso(Base):
    __tablename__='ingresos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    valorIngreso = Column(Integer)
    descripcionIngreso = Column(String(200))
    fechaIngreso = Column(Date)
    pass