from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit

class RegisterationForm(UserCreationForm):
	def __init__(self, *args, **kwargs):
		super(RegisterationForm, self).__init__(*args, **kwargs)

		self.helper = FormHelper()
	    #self.helper.form_id = 'id-exampleForm'
        #self.helper.form_class = 'blueForms'
		self.helper.form_method = 'post'
		self.helper.form_action = '/accounts/register'
		self.helper.layout = Layout(
			'username',
			'password1',
			'password2',
			ButtonHolder(
				Submit('register', 'Register', css_class='btn-primary')
			)

		)


class LoginForm(AuthenticationForm):
	def __init__(self, *args, **kwargs):
		super(LoginForm, self).__init__(*args, **kwargs)

		self.helper = FormHelper()
		self.helper.form_method = 'post'
		#self.helper.form_action = ''
		self.helper.layout = Layout(
			'username',
			'password',
			ButtonHolder(
				Submit('register', 'Register', css_class='btn-primary')
			)

		)