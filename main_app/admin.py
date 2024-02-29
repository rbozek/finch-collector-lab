from django.contrib import admin
# import my models here
from .models import Monkey, Brushing, Accessory

# Register my models here
admin.site.register(Monkey)
admin.site.register(Brushing)
admin.site.register(Accessory)
