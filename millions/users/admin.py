from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'gender']

    class Meta:
        verbose_name = 'user_list'
        verbose_name_plural = "user_list"

admin.site.register(User, UserAdmin)
