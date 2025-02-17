# TODO: Agrega el código de las clases del modelo aquí. Borra este comentario al terminar.

from _datetime import datetime


class Note:
    HIGH: str = "HIGH"
    MEDIUM: str = "MEDIUM"
    LOW: str = "LOW"

    def __init__(self, code: str, title: str, text: str, importance: str, ):
        self.code: str = code
        self.title: str = title
        self.text: str = text
        self.importance: str = importance
        self.creation_date: datetime = datetime.datetime.now()
        self.tags: list = []

    def add_tag (self, tag:str ):
        if tag not in self.tags: