from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class Alumno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    apellidoPaterno = db.Column(db.String(50))
    apellidoMaterno = db.Column(db.String(50))
    email = db.Column(db.String(50))
    edad = db.Column(db.Integer)
    fecha_registro = db.Column(db.DateTime, default=datetime.datetime.now)
