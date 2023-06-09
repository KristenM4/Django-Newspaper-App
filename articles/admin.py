from django.contrib import admin
from .models import Article, Comment

# Register your models here.

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0

class ArticleAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "author",
        "date",
        "body"
    ]
    list_filter = ("author", "date",)
    inlines = [CommentInline,]


class CommentAdmin(admin.ModelAdmin):
    list_display = [
        "article",
        "comment",
        "author",
        "date",
    ]
    list_filter = ("article", "date", "author")

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)