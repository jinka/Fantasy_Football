from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField,BooleanField, RadioField
from wtforms.validators import Required,Email,EqualTo
from ..models import User
from wtforms import ValidationError


class LoginForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    password = PasswordField('Password',validators =[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()],)
    username = StringField('Enter your username',validators = [Required()])
    phone = StringField('Phone', validators=[Required()])
    interest = RadioField('Select Choice', choices=[('fixture','Fixtures'),('live score','Live Games')])
    password = PasswordField('Password',validators = [Required(), EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords',validators = [Required()])
    submit = SubmitField('Sign Up')



    def validate_email(self,data_field):
            if User.query.filter_by(email = data_field.data).first():
                raise ValidationError('There is an account with that email')

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('User Name already exist in the database.')

    def validate_phone(self, data_field):
        if len(data_field.data) > 16:
            raise ValidationError('Invalid phone number.')
        try:
            input_number = phone.parse(data_field.data)
            if not (phone.is_valid_number(input_number)):
                raise ValidationError('Invalid phone number.')
        except:
            input_number = phone.parse("+1"+data_field.data)
            if not (phone.is_valid_number(input_number)):
                raise ValidationError('Invalid phone number.')        
        