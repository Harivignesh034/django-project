from django.contrib import admin
from .models import RegisteredForms,OrderForm

# Register your models here.
admin.site.register(RegisteredForms)
admin.site.register(OrderForm)