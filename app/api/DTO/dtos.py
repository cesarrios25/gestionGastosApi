from pydantic import BaseModel, Field
from datetime import date

# los dto son clases que establecen el modelo de transferencia de datos.
class UsuarioDTOPeticion(BaseModel):
    nombres: str
    edad: int
    telefono: str
    correo: str
    contraseña: str
    fechaRegistro: date
    ciudad: str
    metaAhorro: float
    class Config:
        orm_mode = True
    

class UsuarioDTORespuesta(BaseModel):
    id: int
    nombres: str
    metaAhorro: float
    class Config:
        orm_mode = True



class GastoDTOPeticion(BaseModel):
    descripcionGasto: str
    valorGastado: int
    fechaGasto: date
    class Config:
        orm_mode = True

class GastoDTORespuesta(BaseModel):
    id: int
    descripcionGasto: str
    valorGastado: int
    fechaGasto: date
    class Config:
        orm_mode = True


class CategoriaDTOPeticion(BaseModel):
    nombre: str
    descripcionCategoria: str
    imagenRuta: str
    class Config:
        orm_mode = True

class CategoriaDTORespuesta(BaseModel):
    id: int
    nombre: str
    descripcionCategoria: str
    imagenRuta: str
    class Config:
        orm_mode = True


class IngresoDTOPeticion(BaseModel):
    valorIngreso: int
    descripcionIngreso: str
    fechaIngreso: date
    class Config:
        orm_mode = True

class IngresoDTORespuesta(BaseModel):
    id: int
    valorIngreso: int
    descripcionIngreso: str
    fechaIngreso: date
    class Config:
        orm_mode = True