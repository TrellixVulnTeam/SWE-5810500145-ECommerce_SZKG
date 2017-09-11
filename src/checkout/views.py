from django.shortcuts import render
from django.conf import settings


from django.contrib.auth.decorators import login_required
# Create your views here.
import stripe


stripe.api_key = settings.STRIPE_SECRET_KEY
@login_required
def checkout(request):
    publishKey = settings.STRIPE_PUBLISHABLE_KEY
    customer_id = request.user.userstripe.stripe_id
    if request.method == 'POST':
        token = request.POST('stripeToken')
        customer = stripe.Customer.retrieve(customer_id)
        customer.sources.create(source={token})
        charge = stripe.Charge.create(
                amount=1000,
                currency="usd",
                description="Example charge",
                customer = customer
        )
    context = {'publishKey': publishKey}
    template = 'checkout.html'
    return render(request, template, context)
def checkout_complete(req):
    template = 'checkout_complete.html'
    return render(req, template)