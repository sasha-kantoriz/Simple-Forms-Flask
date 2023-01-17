from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, BooleanField, SelectField, RadioField
from wtforms.widgets import TextArea


class BaseMemberForm(FlaskForm):
    role = SelectField('Peran:', choices=[('grand', 'Kakek / Nenek'), ('adult', 'Anak'), ('child', 'Cucu'), ('grandchild', 'Cicit')], id='role')
    gender = RadioField('Jenis Kelamin:', choices=[('male', 'Pria'), ('female', 'Perempuan')], id='gender')
    full_name = StringField('Nama Lengkap:', id='full_name')
    date_of_birth = StringField('Tanggal Lahir:', id='date_of_birth')
    place_of_birth = StringField('Tempat Lahir:', id='place_of_birth')
    complete_address = StringField('Alamat Lengkap:', id='complete_address', widget=TextArea())
    deceased = BooleanField('Almarhum:', id='deceased')
    #
    mother_id = SelectField('Nama lengkap Ibu:', id='mother_id')
    father_id = SelectField('Nama lengkap Ayah:', id='father_id')
    #
    husbands_full_name = StringField('Nama lengkap Suami:', id='husbands_full_name')
    wifes_full_name = StringField('Nama lengkap Istri:', id='wifes_full_name')
    inlaws_full_name = StringField('Nama lengkap Menantu:', id='inlaws_full_name')
    father_inlaws_full_address = StringField('Alamat lengkap Mertua:', id='father_inlaws_full_address', widget=TextArea())


class ChildMemberForm(BaseMemberForm):
    pass


class AdultMemberForm(BaseMemberForm):
    pass


class LoginForm(FlaskForm):
    password = PasswordField('Password:', id='password')
