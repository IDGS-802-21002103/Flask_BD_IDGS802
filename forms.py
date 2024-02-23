'''Modulo para la creacion de formularios'''

from wtforms import Form
from wtforms import RadioField
from wtforms import StringField
from wtforms import EmailField
from wtforms import SelectField
from wtforms import validators

class  UserForm(Form):
    '''Formulario para el registro de usuarios'''
    nombre = StringField('Nombre', [validators.DataRequired(message='El campo es requerido'), validators.length(min=4, max=10, message='Ingrese un nombre valido')])
    apellido = StringField('Apellido')
    email = EmailField('Email', [validators.DataRequired(message='El campo es requerido'), validators.Email(message='Ingrese un email valido')])
    # materias = SelectField(choices=[('Espanol','Esp'), ('Matematicas','Mat'), ('Ingles','Ing')])
    # radios = RadioField('Curso', choices=[('1','1'), ('2','2'), ('3','3'), ('4','4'), ('5','5')])
    edad = StringField('Edad', [validators.DataRequired(message='El campo es requerido'), validators.length(min=1, max=2, message='Ingrese una edad valida')])
