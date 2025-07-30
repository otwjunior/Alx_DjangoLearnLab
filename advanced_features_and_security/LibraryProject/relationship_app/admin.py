from django.contrib import admin
from .models import  UserProfile
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(CustomUser)