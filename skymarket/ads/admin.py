from django.contrib import admin

from ads.models import Ad, Comment


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "price", "description", "author")
    list_display_links = ("pk", "title")
    search_fields = ("title", "description")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("pk", "author", "ad")
    list_display_links = ("pk", "author")
    search_fields = ("author", "ad")
