from bson import ObjectId

from Config.db import collection
from Config.frecuency_medition import realizar_medicion
from Models.Medition import Medition
import datetime


# Las entidades son los modelos que se enviaran y recibiran de la base de datos. Tambien se conocen como DTO.
# Tambien se conocen como DTO (data transfer objects).
def meditionEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "frecuency": item["frecuency"],
        "location": item["location"],
        "hour": item["hour"],
        "date": item["date"],
    }


def meditionsEntity(entity) -> list:
    meditions = []
    for item in entity:
        meditions.append(meditionEntity(item))
    return meditions


def get_all():
    return meditionsEntity(collection.find())


def get_by_id(id: str):
    return meditionEntity(collection.find_one({"_id": ObjectId(id)}))


def new(lugar: str):
    frec = realizar_medicion()

    horas = datetime.datetime.now().time().hour
    minutos = datetime.datetime.now().time().minute
    segundos = datetime.datetime.now().time().second
    hora = str(horas)+":"+str(minutos)+":"+str(segundos)

    dias = datetime.datetime.now().date().day
    mes = datetime.datetime.now().date().month
    anio = datetime.datetime.now().date().year
    fecha = str(dias)+"/"+str(mes)+"/"+str(anio)

    new_medition = {
        "frecuency": frec,
        "location": lugar,
        "hour": hora,
        "date": fecha
    }
    id = collection.insert_one(new_medition).inserted_id
    medition = collection.find_one({"_id": id})
    return meditionEntity(medition)


def update_by_id(id: str, medition: Medition):
    meditionEntity(collection.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(medition)}))
    return meditionEntity(collection.find_one({"_id": ObjectId(id)}))


def delete_by_id(id: str):
    meditionEntity(collection.find_one_and_delete({"_id": ObjectId(id)}))
