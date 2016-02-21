from __future__ import absolute_import


#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from django.http import HttpResponseRedirect  
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import RegisterationForm, LoginForm

from braces import views


class HomePageView(generic.TemplateView):
	template_name = 'home.html'



class SignUpView(
	
	views.AnonymousRequiredMixin,
	views.FormValidMessageMixin,
	generic.CreateView
):
	form_class = RegisterationForm
	form_valid_message = "Thanks for Signing up GO ahead and Login"
	model = User
	template_name = 'accounts/signup.html'


class LoginView(
	views.AnonymousRequiredMixin,
	views.FormValidMessageMixin,
	generic.FormView
	):
	form_class = LoginForm
	form_valid_message = "You have successfully logged in!"
	success_url = reverse_lazy('home')
	template_name = 'accounts/signin.html'

	def form_valid(self, form):
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		user = authenticate(username=username, password=password)

		if user is not None and user.is_active:
			login(self.request, user)
			return super(LoginView, self).form_valid(form)
		else:
			return self.form_invalid(form)

"""
class LogOutView(generic.RedirectView):
	url = reverse_lazy('home')

	def get(self, request, *args, **kwargs):
		logout(request)
		return super(LogOutView, self).get(request, *args , **kwargs)

"""

@login_required
def logout_view(request):
	logout(request)
	messages.success(request, "You have been loged out!")
	return HttpResponseRedirect(reverse_lazy('home'))