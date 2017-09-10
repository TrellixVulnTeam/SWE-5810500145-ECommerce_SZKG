from django.shortcuts import render
from .forms import ContactForm
# Create your views here.
def contact(req):
    form = ContactForm(req.POST or None)
    if form.is_valid():
        print(req.POST)
    context = locals()
    template = 'contact.html'
    return render(req,template,context)