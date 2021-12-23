from django.contrib import admin

# Register your models here.
from .models import Post, Comment

class CommentInline(admin.TabularInline):
    model = Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','status','created_at', 'updated_at')
    list_filter = ('status', 'created_at', )
    search_fields = ['title', 'body',]
    prepopulated_fields = {'slug': ('title',)}
    inlines = [CommentInline, ]

admin.site.register(Post, PostAdmin)