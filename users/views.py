from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from allauth.account.views import SignupView, LoginView, LoginForm


class MySignupView(SignupView):
    template_name = 'signup.html'


class MyloginView(LoginView):
    template_name = 'login.html'


def loginPage(request):
    return render(request, 'login.html')