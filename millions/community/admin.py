from django.contrib import admin

# Register your models here.
from .models import Post
from .models import Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ['title']

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)