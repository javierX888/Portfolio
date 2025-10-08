from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Optional, URL

class ProfileForm(FlaskForm):
    full_name = StringField('Nombre Completo', validators=[Optional(), Length(max=100)])
    profile_picture = StringField('URL de Foto de Perfil', validators=[Optional(), URL(message='Debe ser una URL válida')])
    submit = SubmitField('Actualizar Perfil')
