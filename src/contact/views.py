from django.shortcuts import render

# Create your views here.
def contact(req):
    context = locals()
    template = 'contact.html'
    return render(req,template,context)