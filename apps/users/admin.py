from django.contrib import admin

# Register your models here.
# from apps.users.models import UserProfile
# class UserProfileAdmin(admin.ModelAdmin):
#     pass
# admin.site.register(UserProfile,UserProfileAdmin)

from apps.users.models import UserProfile
from django.contrib.auth.admin import UserAdmin
admin.site.register(UserProfile, UserAdmin)
