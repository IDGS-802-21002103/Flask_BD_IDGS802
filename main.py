"""Archivo principal de la aplicacion"""

from flask import Flask, request, render_template
from flask_wtf.csrf import CSRFProtect
from flask import flash
from config import DevelopmentConfig , csrf
from model import db
import forms

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

@app.errorhandler(404)
def page_not_found(error):
        return render_template('error.html'), 404

@app.route("/")
def index():
    """Funcion inicial de la aplicacion"""
    return render_template("index.html")

@app.route("/maestros")
def maestros():
    """Funcion para mostrar los maestros"""
    return render_template("maestros.html")

@app.route("/alumnos", methods=["GET", "POST"])
def alumnos():
    """Funcion para mostrar los alumnos"""
    alumno_form = forms.UserForm(request.form)
    nombre = ''
    apellido = ''
    email = ''
    print(request.method)
    print("Formulario Valido",alumno_form.validate())
    print(alumno_form.errors)
    
    if request.method == "POST" and alumno_form.validate():
        nombre = alumno_form.nombre.data
        apellido = alumno_form.apellido.data
        email = alumno_form.email.data
        edad = alumno_form.edad.data
        flash("Alumno registrado correctamente")        
        print("Nombre: {}".format(nombre))
        print("Apellido: {}".format(apellido))
        print("Email: {}".format(email))
        
        return render_template("alumnos.html", form=alumno_form, nombre=nombre, apellido=apellido, email=email, edad=edad)
    
    return render_template("alumnos.html", form=alumno_form, nombre='', apellido='', email='', edad='')

if __name__ == "__main__":
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run()
