# importar librerias
from sqlalchemy import create_engine,event
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import Engine

# datos para la conexion a base de datos.
dataBaseName = "gestordb"
userName = "root"
userPass = None
conecctionPort = 3306
server = "localhost"

# creando la conexion
dataBaseConnection = f"mysql+mysqlconnector://{userName}:{userPass}@{server}:{conecctionPort}/{dataBaseName}"

#creo en motor de conexion
engine = create_engine(dataBaseConnection)

# abrir le sesion con la base de datos.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
