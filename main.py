"""Archivo principal de la aplicacion"""

from math import log
import re
from venv import logger
from flask import Flask, redirect, request, render_template, flash, url_for
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from models import db, Alumno


import forms
import logging

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect()


@app.errorhandler(404)
def page_not_found(_):
    """Manejador de error 404"""
    return render_template("error.html"), 404


@app.route("/", methods=["GET", "POST"])
def index():
    """Funcion inicial de la aplicacion"""
    alumno_form = forms.AlumnoForm(request.form)
    if request.method == "POST":
        alumno = Alumno(
                        nombre=alumno_form.nombre.data.upper() ,
                        apellidoPaterno=alumno_form.apellidoPaterno.data.upper() ,
                        apellidoMaterno=alumno_form.apellidoMaterno.data.upper() ,
                        email=alumno_form.email.data.upper()
                        )
        db.session.add(alumno)
        db.session.commit()
    return render_template("index.html", form=alumno_form)


@app.route("/maestros")
def maestros():
    """Funcion para mostrar los maestros"""
    return render_template("maestros.html")


@app.route("/alumnos", methods=["GET", "POST"])
def alumnos_form():
    """Funcion para mostrar los alumnos"""
    alumno_form = forms.UserForm(request.form)

    if request.method == "POST" and alumno_form.validate():
        nombre = alumno_form.nombre.data
        apellido = alumno_form.apellido.data

        mensaje = f"Bienvenido: {nombre + ' ' + apellido}"

        flash(mensaje)

    return render_template("alumnos.html", form=alumno_form)


@app.route("/alumnos_tabla", methods=["GET", "POST"])
def tabla_alumnos():
    """Funcion para mostrar la tabla de alumnos"""
    alumno_form = forms.AlumnoForm(request.form)
    alumnos = Alumno.query.all()
    return render_template("alumnos_tabla.html", alumnos=alumnos)


@app.route("/eliminar", methods=["GET", "POST"])
def eliminar():
    '''Funcion para eliminar un alumno'''
    alumno_form = forms.AlumnoForm(request.form)
    if request.method == "GET":
        id = request.args.get("id")
        alumno = db.session.query(Alumno).filter(Alumno.id==id).first()
        alumno_form.id.data = request.args.get("id")
        alumno_form.nombre.data = alumno.nombre
        alumno_form.apellidoPaterno.data = alumno.apellidoPaterno
        alumno_form.apellidoMaterno.data = alumno.apellidoMaterno
        alumno_form.email.data = alumno.email

    if request.method == "POST":
        id = alumno_form.id.data
        alumno = Alumno.query.get(id)
        if alumno is None:
            flash("Alumno no encontrado.")
            return redirect(url_for("tabla_alumnos"))
        db.session.delete(alumno)
        db.session.commit()
        return redirect(url_for("tabla_alumnos"))

    return render_template("eliminar.html", form=alumno_form)


@app.route("/modificar", methods=["GET", "POST"])
def modificar():
    """Funcion para eliminar un alumno"""
    alumno_form = forms.AlumnoForm(request.form)
    if request.method == "GET":
        id = request.args.get("id")
        alumno = db.session.query(Alumno).filter(Alumno.id == id).first()
        alumno_form.id.data = request.args.get("id")
        alumno_form.nombre.data = alumno.nombre
        alumno_form.apellidoPaterno.data = alumno.apellidoPaterno
        alumno_form.apellidoMaterno.data = alumno.apellidoMaterno
        alumno_form.email.data = alumno.email

    if request.method == "POST":
        id = alumno_form.id.data
        alumno = Alumno.query.get(id)
        if alumno is None:
            flash("Alumno no encontrado.")
            return redirect(url_for("tabla_alumnos"))
        alumno.nombre = alumno_form.nombre.data
        alumno.apellidoPaterno = alumno_form.apellidoPaterno.data   
        alumno.apellidoMaterno = alumno_form.apellidoMaterno.data
        alumno.email = alumno_form.email.data
        
        db.session.add(alumno)
        db.session.commit()
        return redirect(url_for("tabla_alumnos"))

    return render_template("modificar.html", form=alumno_form)


if __name__ == "__main__":
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(port=8000)
