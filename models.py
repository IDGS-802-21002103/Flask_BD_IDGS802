'''Archivo que contiene el modelo de la tabla alumno'''
import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Alumno(db.Model):
    '''Modelo de la tabla alumno'''
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    apellidoPaterno = db.Column(db.String(50))
    apellidoMaterno = db.Column(db.String(50))
    email = db.Column(db.String(50))
    fecha_registro = db.Column(db.DateTime, default=datetime.datetime.now)
