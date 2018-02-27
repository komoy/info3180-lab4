from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField
from wtforms.validators import DataRequired
ALLOWED_EXTENSIONS = [ 'png', 'jpg', 'jpeg', 'gif']

class UploadForm(FlaskForm):
    ALLOWED_EXTENSIONS = [ 'png', 'jpg', 'jpeg', 'gif']

    upload = FileField('image', validators=[FileRequired(),FileAllowed(ALLOWED_EXTENSIONS, 'Images only!')])