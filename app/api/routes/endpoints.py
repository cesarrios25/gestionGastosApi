from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from typing import List
from fastapi.params import Depends

from app.api.DTO.dtos import UsuarioDTOPeticion, UsuarioDTORespuesta, GastoDTOPeticion, GastoDTORespuesta, CategoriaDTOPeticion, CategoriaDTORespuesta, IngresoDTOPeticion, IngresoDTORespuesta
from app.api.models.tablasSQL import Usuario, Gasto, Categoria, Ingreso
from app.database.configuration import sessionLocal, engine

rutas = APIRouter()

def conectarConBd():
    try:
        baseDatos = sessionLocal()
        yield baseDatos
    except Exception as error:
        baseDatos.rollback()
        raise error
    finally:
        baseDatos.close()

# CONSTRUYENDO NUESTROS SERVICIOS

# cada servico (operacion o transaccion bd) debe programarse como una funcion que reciba como parametro la sesion de la base de datos.

# USUARIO

# asignar un endpoint
@rutas.post('/usuario',response_model=Usuario, summary='Registrar un usuario en la base de datos')

def guardarUsuario(datosUsuario:UsuarioDTOPeticion, database:Session=Depends(conectarConBd)):
    try:
        usuario = Usuario(
            nombres = datosUsuario.nombres,
            fechaRegistro = datosUsuario.fechaRegistro,
            ciudad = datosUsuario.ciudad,
            metaAhorro = datosUsuario.metaAhorro
        )
        # ordenandole a la bd
        database.add(usuario)
        database.commit()
        database.refresh(usuario)
        return usuario
    
    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400, detail=f"Tenemos un problema {error}")

# para buscar no necesito datos solo la conexion
@rutas.get('/usuario', response_model=List[UsuarioDTORespuesta], summary='Buscar todos los usuarios en base de datos')
def buscarUsuarios(database:Session=Depends(conectarConBd)):
    try:
        usuarios = database.query(Usuario).all()
        return usuarios
    
    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400, detail=f"No se pueden buscar los usuarios {error}")

# GASTO

# asignar un endpoint
@rutas.post('/gastos',response_model=Usuario, summary='Registrar un usuario en la base de datos')

def guardarGastos(gastosUsuario:GastoDTOPeticion, database:Session=Depends(conectarConBd)):
    try:
        gasto = Gasto(
            descripcionGasto = gastosUsuario.descripcionGasto,
            valorGastado = gastosUsuario.valorGastado,
            fechaGasto = gastosUsuario.fechaGasto
        )
        # ordenandole a la bd
        database.add(gasto)
        database.commit()
        database.refresh(gasto)
        return gasto
    
    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400, detail=f"Tenemos un problema {error}")

# para buscar no necesito datos solo la conexion
@rutas.get('/gastos', response_model=List[GastoDTORespuesta], summary='Buscar todos los usuarios en base de datos')
def buscarGastos(database:Session=Depends(conectarConBd)):
    try:
        gastos = database.query(Gasto).all()
        return gastos
    
    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400, detail=f"No se pueden buscar los usuarios {error}")
    


# CATEGORIA

# asignar un endpoint
@rutas.post('/categorias',response_model=Usuario, summary='Registrar un usuario en la base de datos')

def guardarCategoria(categoriaUsuario:CategoriaDTOPeticion, database:Session=Depends(conectarConBd)):
    try:
        categoria = Categoria(
            nombre = categoriaUsuario.nombre,
            descripcionCategoria = categoriaUsuario.descripcionCategoria,
            imagenRuta = categoriaUsuario.imagenRuta,
        )
        # ordenandole a la bd
        database.add(categoria)
        database.commit()
        database.refresh(categoria)
        return categoria
    
    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400, detail=f"Tenemos un problema {error}")

# para buscar no necesito datos solo la conexion
@rutas.get('/categorias', response_model=List[UsuarioDTORespuesta], summary='Buscar todos los usuarios en base de datos')
def buscarUsuarios(database:Session=Depends(conectarConBd)):
    try:
        categorias = database.query(Categoria).all()
        return categorias
    
    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400, detail=f"No se pueden buscar los usuarios {error}")


# INGRESO

# asignar un endpoint
@rutas.post('/ingresos',response_model=Usuario, summary='Registrar un ingreso en la base de datos')

def guardarIngreso(ingresoUsuario:IngresoDTOPeticion, database:Session=Depends(conectarConBd)):
    try:
        ingreso = Ingreso(
            valorIngreso = ingresoUsuario.valorIngreso,
            descripcionIngreso = ingresoUsuario.descripcionIngreso,
            fechaIngreso = ingresoUsuario.fechaIngreso,
        )
        # ordenandole a la bd
        database.add(ingreso)
        database.commit()
        database.refresh(ingreso)
        return ingreso
    
    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400, detail=f"Tenemos un problema {error}")

# para buscar no necesito datos solo la conexion
@rutas.get('/ingresos', response_model=List[IngresoDTORespuesta], summary='Buscar todos los ingresos en base de datos')
def buscarIngreso(database:Session=Depends(conectarConBd)):
    try:
        ingresos = database.query(Ingreso).all()
        return ingresos
    
    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400, detail=f"No se pueden buscar los ingresos {error}")
