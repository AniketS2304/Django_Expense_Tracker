from django.contrib import admin

# Register your models here.

from user_auth.models import * 

class UserAdmin(admin.ModelAdmin):
    list_display = [
    "name",
    "email",
    # "password"
    ]

admin.site.register(User, UserAdmin)