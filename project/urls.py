from django.conf.urls import include, url
from django.contrib import admin
 
from views import HomePageView, SignUpView, LoginView
from views import logout_view

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HomePageView.as_view(), name = 'home'),
    url(r'^accounts/register', SignUpView.as_view(success_url="/"), name = 'signup'),
    url(r'^accounts/signin', LoginView.as_view(),name = 'signin'),
    url(r'^accounts/signout', logout_view, name = 'signout'),

]
