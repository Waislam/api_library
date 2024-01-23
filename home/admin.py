from django.contrib import admin
from .models import Category, App, Api

# Register your models here.
admin.site.register(Category)
admin.site.register(App)
admin.site.register(Api)
