import pymongo
from dotenv import load_dotenv
import os

# Para trabajar con mongo como base de datos y guardar el link de mongo cloud en variables de entorno
# el link de mi base de datos es:
# mongodb+srv://usuario:usuario@instrumentacion.fgmakck.mongodb.net/?retryWrites=true&w=majority
# lo coloco aqui porque esto es un proyecto de prueba.

# se cargan las variables del entorno, en mi caso
# la variable db-URI tiene el link
load_dotenv()
URI = os.environ.get("db-URI")

# a taves de pymongo se realizara la coneccion a la base de datos.
# direccion del cliente de mongodb
conn = pymongo.MongoClient(URI)
# nombre de la base de datos a la que nos vamos a conectar o a crear
mydb = conn["develop"]
# nombre de la coleccion a conectar o a crear
collection = mydb.get_collection("meditions")