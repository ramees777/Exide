from django.contrib import admin
from . models import user_register
from . models import purchase_details
from . models import battery_details

admin.site.register(user_register)
admin.site.register(purchase_details)
admin.site.register(battery_details)