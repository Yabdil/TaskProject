from django.contrib import admin
from .models import Task, CustomModel

# Register your models here.

admin.site.register(Task)
admin.site.register(CustomModel)