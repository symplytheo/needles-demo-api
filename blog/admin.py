from django.contrib import admin
from .models import Category, Post, Comment, Reply


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug", "created_at", "updated_at")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name", "id")
    ordering = ("-created_at",)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "slug", "category", "created_at", "updated_at")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "id", "category")
    ordering = ("-created_at",)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "message", "post", "created_at")
    ordering = ("-created_at",)


@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "message", "comment", "created_at")
    ordering = ("-created_at",)
