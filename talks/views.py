from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.views import generic

from . import models
from . import forms

from braces import views

class RestrictToUserMixin(views.LoginRequiredMixin):
	def get_queryset(self):
		queryset = super(RestrictToOwnerMixin, self).get_queryset()
		queryset = queryset.filter(user=self.request.user)
		return queryset


class TalkListListView(
	views.LoginRequiredMixin,
	generic.ListView
):
	model = models.TalkList

	def get_queryset(self):
		return self.request.user.lists.all()



class TalkListDetailView(
	views.LoginRequiredMixin,
	#views.PrefetchRelatedMixin,
	generic.DetailView
):
	model = models.TalkList
	prefetch_related = ('talks',)


	def get_queryset(self):
		queryset = super(TalkListDetailView, self).get_queryset()
		queryset = queryset.filter(user=self.request.user)
		return queryset


class TalkListCreateView(
	views.LoginRequiredMixin,
	views.SetHeadlineMixin,
	generic.CreateView
):
	
	form_class = forms.TalkListForm
	headline = 'Create'
	model = models.TalkList

	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.user = self.request.user
		self.object.save()
		return super(TalkListCreateView, self).form_valid(form)



class TalkListUpdateView(
	#RestrictToOwnerMixin,
	views.LoginRequiredMixin,
	views.SetHeadlineMixin,
	generic.UpdateView
):
	form_class = forms.TalkListForm
	headline = 'Update'
	model = models.TalkList

	def get_queryset(self):
		queryset = super(RestrictToOwnerMixin, self).get_queryset()
		queryset = queryset.filter(user=self.request.user)
		return queryset
