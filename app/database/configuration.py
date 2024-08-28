# deja accede a la base de datos.
# datos para la conexion a base de datos.
dataBaseName = "gestordb"
userName = "root"
userPass = None
conecctionPort = 3306
server = "localhost"

# creando la conexion
dataBaseConnection = f"mysql+mysqlconnector://{userName}:{userPass}@{server}:{conecctionPort}/{dataBaseName}"
print(dataBaseConnection)