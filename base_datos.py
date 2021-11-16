from peewee import *
import datetime


db = SqliteDatabase("baseprueba3.db")


class BaseModel(Model):
    class Meta:
        database = db


class Noticia(BaseModel):
    id = BigIntegerField(primary_key=True, unique=True)
    titulo = CharField(128)
    descripcion = TextField()
    fecha = DateTimeField(default=datetime.datetime.now)
    estado = BooleanField(default=True)


class Log(BaseModel):
    fecha = DateTimeField(default=datetime.datetime.now)
    id = TextField()
    titulo = CharField(128)
    descripcion = TextField()


db.connect()
db.create_tables([Noticia, Log])
