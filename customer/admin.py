from django.contrib import admin
from customer.models import Customer, Employee, Credentials, Device

admin.site.register(Customer)
admin.site.register(Employee)
admin.site.register(Device)


@admin.register(Credentials)
class CredentialsAdmin(admin.ModelAdmin):
    list_display = ("name", "api_key")
