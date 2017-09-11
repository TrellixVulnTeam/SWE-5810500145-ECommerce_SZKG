from django.contrib import admin
from .models import Profile, userStripe
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    class Meta:
        model = Profile



class userStripeAdmin(admin.ModelAdmin):
    model = userStripe


admin.site.register(Profile,ProfileAdmin)
admin.site.register(userStripe, userStripeAdmin)