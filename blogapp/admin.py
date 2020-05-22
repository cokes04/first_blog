from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ["pk","author","title","text","create_date","published_date"]

admin.site.register(Post,PostAdmin)