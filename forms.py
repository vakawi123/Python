from flask_wtf import FlaskForm
from wtforms.fields import StringField, EmailField, DateField,PasswordField, RadioField, SelectField, IntegerField,SubmitField
from wtforms.validators import DataRequired,length,equal_to

class DeliveryForm(FlaskForm):
    name = StringField("input Full Name", validators=[DataRequired()])
    lastname = StringField("input your Lastname", validators=[DataRequired()])
    email = EmailField("input Email", validators=[DataRequired()])
    phone_number = IntegerField("Phone number", validators=[DataRequired(), length(min=7, max=15)])

    country = SelectField("choose country", choices = ["Select Country", "Georgia", "Austia", "Turkey", "USA", "Egypt", "UK", "France"], validators=[DataRequired()])
    region = StringField("input your Region,State...", validators=[DataRequired()])
    city = StringField("Your City" , validators=[DataRequired()])
    address = StringField("input your address" , validators=[DataRequired()])
    post_code = IntegerField("postal code :" , validators=[DataRequired(), length(min=5, max=7)])

    delivery = SubmitField("Delivery")

class ProductForm(FlaskForm):
    name = StringField("input name", validators=[DataRequired()])
    price = IntegerField("input price", validators=[DataRequired()])
    country = StringField("input Country" , validators=[DataRequired()])

    add = SubmitField("Add product")

class RegisterForm(FlaskForm):
    email = StringField("input email", validators=[DataRequired()])
    username = StringField("input username", validators=[DataRequired()])
    password = PasswordField("input password", validators=[DataRequired(), length(min=7, max=20)])
    repeat_password = PasswordField("repeat password",validators=[DataRequired(), equal_to("password")])
    birthday = DateField("input birthday", validators=[DataRequired()])

    register = SubmitField("Register")

class LoginForm(FlaskForm):
    username = StringField("input username",validators=[DataRequired()])
    password = PasswordField("input password", validators=[DataRequired()])

    login = SubmitField("Login")



