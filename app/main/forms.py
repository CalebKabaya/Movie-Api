from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import DataRequired
from wtforms.validators import Required

class ReviewForm(FlaskForm):

    title = StringField('Review title',validators=[DataRequired()])
    review = TextAreaField('Movie review', validators=[DataRequired()])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio= TextAreaField('Tells us about you.',validators=[Required()])
    submit= SubmitField('Submit') 
class ReviewForm(FlaskForm):

    title = StringField('Review title',validators=[Required()])
    review = TextAreaField('Movie review')
    submit = SubmitField('Submit')       