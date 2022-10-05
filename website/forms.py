from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import DataRequired, Email


class RecipeForm(FlaskForm):

    # name
    # ingredients
    # instructions
    # image

    name = StringField("Recipe Name", validators=[DataRequired()])
    ingredients = StringField("Ingredients", validators=[DataRequired()])
    instructions = StringField("Instructions", validators=[DataRequired()])
    image = FileField('Image', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'jpg, png Images only!')
                                           ])
    submit = SubmitField("Submit")


class LoginForm(FlaskForm):

    # email
    # password

    email = EmailField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])

    submit = SubmitField("Login")


class SignupForm(FlaskForm):

    # email
    # username
    # password1
    # password2

    email = EmailField("Email", validators=[DataRequired(), Email()])
    username = StringField("User Name", validators=[DataRequired()])
    password1 = PasswordField("Password", validators=[DataRequired()])
    password2 = PasswordField("Confirm Password", validators=[DataRequired()])

    submit = SubmitField("Signup")
