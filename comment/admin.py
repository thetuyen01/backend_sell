from django.contrib import admin
from .models import Comment

class CommentAdmin(admin.ModelAdmin):
    # Define fields you want to display in the admin interface
    list_display = ('product', 'name', 'title', 'rating', 'created_at')
    # Optionally, you can define search fields
    search_fields = ('name', 'title')
    # Optionally, you can filter comments by product
    list_filter = ('product',)

admin.site.register(Comment, CommentAdmin)
