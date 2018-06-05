from django.conf.urls import url, include
from django.views.generic.base import TemplateView

from allauth.account.views import SignupView, LoginView


class MySignupView(SignupView):
    template_name = 'my_signup.html'


class MyLoginView(LoginView):
    template_name = 'my_login.html'


urlpatterns = [
    # url(r'^account/$', views.index, name='index'),
    url(r'^', include('allauth.urls')),
    url(r'^profile', TemplateView.as_view(template_name='profile.html')),
    url(r'^login', TemplateView.as_view(template_name='login.html')),
    url(r'^signup', TemplateView.as_view(template_name='signup.html')),

]