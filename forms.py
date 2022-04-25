from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField, SelectField, FloatField, DecimalField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Email, Length
from datetime import date

class SignupForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(max=64)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    fullname = StringField('fullname', validators=[DataRequired(), Length(max=64)])

    submit = SubmitField('Submit')

    start_date = DateField("Start date", default=date.today(), format='%Y-%m-%d', validators=[DataRequired(message="You need to enter the start date")])
    #end_date = DateField("End date", default=date.today(), format='%d/%m/%Y', validators=[DataRequired(message="You need to enter the end date.")])
    #hier alle weiteren Felder auflisten um das listing durchzuführen

#https://stackoverflow.com/questions/30955801/wtforms-how-to-attach-json-data-to-the-request
#https://wtforms.readthedocs.io/en/latest/fields/
#https://specialistoff.net/page/283

# Parametisierung notwendig

class ListingForm(FlaskForm):
    listing_title = StringField('listing_title', validators=[DataRequired(message="Name of your publication required"), Length(min=4, max=80)])
    listing_domain = StringField('listing_domain', validators=[DataRequired(message="URL of your business required"), Length(max=80)])
    listing_description = TextAreaField('listing_description', validators=[DataRequired(), Length(min=40, max=800)])
    listing_price = DecimalField('listing_price', places=0, validators=[DataRequired()])
    listing_type = SelectField('listing_type', choices=[('Buy', 'Buy Now'), ('Auction', 'Auction'), ('Offer', 'Receive Offers')])
    listing_special = SelectField('listing_special', choices=[('Feature1W', 'Feature 1 week'), ('Feature2W', 'Feature 2 week'), ('Feature4W', 'Feature 4 weeks')])

    submit = SubmitField('Submit')

    # start_date = DateField("Start date", default=date.today(), format='%Y-%m-%d',
    #                        validators=[DataRequired(message="You need to enter the start date")])
