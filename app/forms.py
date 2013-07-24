from flask.ext.wtf import Form, TextField, BooleanField
from flask.ext.wtf import Required
# Required checks that fiels is not submitted empty 

class LoginForm(Form):
	openid = TextField('openid', validators = [Required()])
	remember_me = BooleanField('remember_me', default = False)
