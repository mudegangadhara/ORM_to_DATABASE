from django.contrib import admin

# Register your models here.
from app.models import *
admin.site.register(Student)
admin.site.register(Coures)
admin.site.register(Accessmode)