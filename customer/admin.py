from django.contrib import admin
from customer.models import Customer, Employee, Credentials

admin.site.register(Customer)
admin.site.register(Employee)
admin.site.register(Credentials)
