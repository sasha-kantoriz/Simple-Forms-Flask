from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, BooleanField, SelectField, RadioField
from wtforms.widgets import TextArea


class BaseMemberForm(FlaskForm):
    role = SelectField('Role:', choices=[('grand', 'Grand'), ('adult', 'Adult'), ('child', 'Child'), ('grandchild', 'Grandchild')], id='role')
    gender = RadioField('Gender:', choices=[('male', 'Male'), ('female', 'Female')], id='gender')
    full_name = StringField('Full Name:', id='full_name')
    date_of_birth = StringField('Date of Birth:', id='date_of_birth')
    place_of_birth = StringField('Place of Birth:', id='place_of_birth')
    complete_address = StringField('Complete Address:', id='complete_address', widget=TextArea())
    deceased = BooleanField('Deceased:', id='deceased')
    #
    mother_id = SelectField('Mother:', id='mother_id')
    father_id = SelectField('Father:', id='father_id')
    #
    husbands_full_name = StringField('Husbands Full Name:', id='husbands_full_name')
    wifes_full_name = StringField('Wifes Full Name:', id='wifes_full_name')
    inlaws_full_name = StringField('Inlaws Full Name:', id='inlaws_full_name')
    father_inlaws_full_address = StringField('Father Inlaws Full Address:', id='father_inlaws_full_address', widget=TextArea())


class ChildMemberForm(BaseMemberForm):
    pass


class AdultMemberForm(BaseMemberForm):
    pass


class LoginForm(FlaskForm):
    password = PasswordField('Password:', id='password')
