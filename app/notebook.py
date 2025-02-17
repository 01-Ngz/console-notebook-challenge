# TODO: Agrega el código de las clases del modelo aquí. Borra este comentario al terminar.

from _datetime import datetime


class Note:
    HIGH: str = "HIGH"
    MEDIUM: str = "MEDIUM"
    LOW: str = "LOW"

    def __init__(self, code: str, title: str, text: str, importance: str, ):
        self.code: str = code # Codificacion
        self.title: str = title # Titulo
        self.text: str = text # Texto
        self.importance: str = importance # Importancia
        self.creation_date: datetime = datetime.now() #Creacion de fecha y hora actual
        self.tags: list = [] # Etiquetas

    def add_tag (self, tag:str ):
        #Agregar la etiqueta a la lista, si no esta presente
        if tag not in self.tags: # Se verifica que no este en la lista
            self.tags.append(tag) #Agregamos la etiqueta
            return tag


    def __str__(self, Date)-> str:
        self.Date: str  = Date
        return f"Date: {self.creation_date}\n {self.title}: {self.text}" #Cadena de cararcteres, \n para separar lineas de codigo



class Notebook:
    def __init__(self):
        self.notes: list[Note] = []


    def add_note(self, title: str, text: str, importance: str, ) -> int:

        #genereamos el nuevo codigo: numero de notas existentes + 1
        new_codigo = len(self.notes)

        #Creamos nueva nota
        new_note = Note(new_codigo, title, text, importance)
        #agregamos a la lista de notas
        self.notes.append(new_note)
        return new_codigo


    def note (self, notes:list[Note]):

