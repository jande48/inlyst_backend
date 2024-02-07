from django.contrib import admin
from customer.models import Customer, Employee, Credentials, Device

admin.site.register(Customer)
admin.site.register(Employee)
admin.site.register(Credentials)
admin.site.register(Device)
