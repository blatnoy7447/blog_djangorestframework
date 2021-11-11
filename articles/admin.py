from django.contrib import admin

from .models import Post, Review, CustomUser


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "title", "created_at")
    list_display_links = ("title",)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "text",)
    list_display_links = ("text",)


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email", "is_staff")
    list_display_links = ("username",)

