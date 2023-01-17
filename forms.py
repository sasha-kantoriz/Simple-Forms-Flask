from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, BooleanField, SelectField, RadioField
from wtforms.widgets import TextArea


class BaseMemberForm(FlaskForm):
    role = SelectField('Peran:', choices=[('grand', 'Gen 1'), ('adult', 'Gen 2'), ('child', 'Gen 3'), ('grandchild', 'Gen 4')], id='role')
    gender = RadioField('Jenis Kelamin:', choices=[('male', 'Pria'), ('female', 'Perempuan')], id='gender')
    full_name = StringField('Nama Lengkap:', id='full_name')
    date_of_birth = StringField('Tanggal Lahir:', id='date_of_birth')
    place_of_birth = StringField('Tempat Lahir:', id='place_of_birth', widget=TextArea())
    complete_address = StringField('Alamat Lengkap:', id='complete_address', widget=TextArea())
    deceased = BooleanField('Almarhum:', id='deceased')
    #
    mother_id = SelectField('Nama lengkap Ibu:', id='mother_id')
    father_id = SelectField('Nama lengkap Ayah:', id='father_id')
    #
    spouse_full_name = StringField('Nama lengkap Suami/Istri:', id='spouse_full_name')
    spouse_date_of_birth = StringField('Tanggal Lahir Suami/Istri:', id='spouse_date_of_birth')
    spouse_place_of_birth = StringField('Tempat Lahir Suami/Istri:', id='spouse_place_of_birth', widget=TextArea())
    inlaws_full_name = StringField('Nama lengkap Mertua:', id='inlaws_full_name')
    father_inlaws_full_address = StringField('Alamat lengkap Mertua:', id='father_inlaws_full_address', widget=TextArea())
    father_inlaws_deceased = BooleanField('Almarhum Mertua:', id='father_inlaws_deceased')


class ChildMemberForm(BaseMemberForm):
    pass


class AdultMemberForm(BaseMemberForm):
    pass


class LoginForm(FlaskForm):
    password = PasswordField('Password:', id='password')
