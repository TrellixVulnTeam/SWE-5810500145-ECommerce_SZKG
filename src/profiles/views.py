from django.shortcuts import render

# Create your views here.
def home(req):
    context = locals()
    template = 'home.html'
    return render(req,template,context)

def about(req):
    context = locals()
    template = 'about.html'
    return render(req,template,context)

def contact(req):
    context = locals()
    template = 'contact.html'
    return render(req,template,context)