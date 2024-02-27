"""Modulo para la creacion de formularios"""

from wtforms import Form
from wtforms import StringField
from wtforms import EmailField
from wtforms import validators


class UserForm(Form):
    """Formulario para el registro de usuarios"""

    REQUIRED_FIELD_MESSAGE = "El campo es requerido"

    nombre = StringField(
        "Nombre",
        [
            validators.DataRequired(message=REQUIRED_FIELD_MESSAGE),
            validators.length(min=4, max=10, message="Ingrese un nombre valido"),
        ],
    )
    apellido = StringField("Apellido")
    edad = StringField(
        "Edad", [validators.number_range(min=1, max=20, message="Valor no valido")]
    )
    email = EmailField(
        "Email",
        [
            validators.DataRequired(message=REQUIRED_FIELD_MESSAGE),
            validators.Email(message="Ingrese un email valido"),
        ],
    )
    edad = StringField(
        "Edad",
        [
            validators.DataRequired(message=REQUIRED_FIELD_MESSAGE),
            validators.length(min=1, max=2, message="Ingrese una edad valida"),
        ],
    )


class AlumnoForm(Form):
    """Formulario para el registro de usuarios"""

    REQUIRED_FIELD_MESSAGE = "El campo es requerido"
    id = StringField("Id", [validators.number_range(min=1, max=20, message="Valor no valido")])
    nombre = StringField(
        "Nombre",
        [
            validators.DataRequired(message=REQUIRED_FIELD_MESSAGE),
            validators.length(min=4, max=10, message="Ingrese un nombre valido"),
        ],
    )
    apellidoPaterno = StringField("Apellido Paterno")
    apellidoMaterno = StringField("Apellido Materno")
    email = EmailField(
        "Email",
        [
            validators.DataRequired(message=REQUIRED_FIELD_MESSAGE),
            validators.Email(message="Ingrese un email valido"),
        ],
    )
