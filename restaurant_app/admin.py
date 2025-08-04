from django.contrib import admin
from .models import Reservation, Contact, Order

admin.site.register(Reservation)
admin.site.register(Contact)
admin.site.register(Order)

