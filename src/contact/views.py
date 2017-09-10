from django.shortcuts import render
from .forms import ContactForm
from django.conf import settings
from django.core.mail import send_mail


# Create your views here.
def contact(req):
    title = 'Contact'
    form = ContactForm(req.POST or None)
    context = {'title':title, 'form':form, }
    if form.is_valid():
        name = form.cleaned_data['name']
        comment = form.cleaned_data['comment']
        subject = 'Message from E-Commerce App'
        message = '%s %s'%(comment, name)
        emailFrom = form.cleaned_data['email']
        emailTo = [settings.EMAIL_HOST_USER]
        send_mail(subject,message,emailFrom,emailTo,fail_silently=True)
    context = locals()
    template = 'contact.html'
    return render(req, template, context)
