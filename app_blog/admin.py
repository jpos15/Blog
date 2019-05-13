from django.contrib import admin
from .models import CategoriaPosts, Posts


@admin.register(CategoriaPosts)
class CategotiaPostsAdmin(admin.ModelAdmin):
    pass


@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    pass