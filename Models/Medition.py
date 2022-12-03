import datetime
from pydantic import BaseModel
from typing import Optional


# Los modelos son las clases que se mapean de la base de datos
# a nuestro lenguaje de programacion para poder trabajar con ellos
class Medition(BaseModel):
    frecuency: float = 0
    location: Optional[str] = None
    hour: Optional[str] = None
    date: Optional[str] = None


