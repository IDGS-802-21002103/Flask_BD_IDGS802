"""Archivo principal de la aplicacion"""

from flask import Flask, request, render_template, flash
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from models import db, Alumno


import forms

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
def alumnos():
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


if __name__ == "__main__":
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run()
