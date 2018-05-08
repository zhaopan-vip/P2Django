from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'pub_date')

class CameraAdmin(admin.ModelAdmin):
    list_display = ('title', 'rtmp', 'm3u8')

# Register your models here.
admin.site.register(Post, PostAdmin)