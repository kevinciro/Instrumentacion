
from typing import List
from fastapi import APIRouter, Response, status
from starlette.status import HTTP_204_NO_CONTENT
from Models.Medition import Medition
from Services.MeditionService import meditionsEntity, meditionEntity, new, delete_by_id, update_by_id, get_by_id, \
    get_all

medition = APIRouter()


# Los controladores o rutas son los medios de comunicacion entre la pagina y la base de datos
# Usan protocolos Http o Https y metodos get para consultar, post para crear, update para actualizar
# y delete para eliminar. Estos 4 metodos constituyen el CRUD basico de una base de datos.

@medition.get('/meditions', response_model=List[Medition], tags=["Meditions"])
def get_all_meditions():
    return get_all()


@medition.get('/meditions/{id}', response_model=Medition, tags=["Meditions"])
def get_medition_by_id(id: str):
    return get_by_id(id)


@medition.post('/meditions', response_model=Medition, tags=["Meditions"])
def post_medition(lugar: str):
    return new(lugar)


@medition.put('/meditions/{id}', response_model=Medition, tags=["Meditions"])
def update_medition_by_id(id: str, medition: Medition):
    return update_by_id(id, medition)


@medition.delete('/medition/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=["Meditions"])
def delete_medition_by_id(id: str):
    delete_by_id(id)
    return Response(status_code=HTTP_204_NO_CONTENT)
