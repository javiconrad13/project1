from wtforms import Form, TextField, SubmitField, FileField, SelectField, validators

class UserForm(Form):
    file = FileField("File",[validators.Required()])
    username = TextField("Username",[validators.required()])
    sex = SelectField("Sex",choices = [("Male","Male"),("Female","Female")])
    fname = TextField("First Name",[validators.required()])
    lname = TextField("Last Name",[validators.required()])
    age = TextField("Age",[validators.required()])
    submit = SubmitField("Enter here")