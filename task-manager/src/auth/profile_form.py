from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Optional

class ProfileForm(FlaskForm):
    full_name = StringField('Nombre Completo', validators=[Optional(), Length(max=100)])
    profile_picture = StringField('URL de Foto de Perfil', validators=[Optional()])
    profile_picture_file = FileField('O sube una foto', validators=[
        Optional(),
        FileAllowed(['jpg', 'jpeg', 'png', 'gif', 'webp'], 'Solo imágenes (JPG, PNG, GIF, WebP)')
    ])
    submit = SubmitField('Actualizar Perfil')
