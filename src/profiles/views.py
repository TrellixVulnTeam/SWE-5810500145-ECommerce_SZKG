from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(req):
    context = {}
    template = 'home.html'
    return render(req, template, context)


def about(req):
    context = {}
    template = 'about.html'
    return render(req, template, context)

@login_required
def userProfile(req):
    user = req.user
    context = {'user':user}
    template = 'profile.html'
    return render(req, template, context)
