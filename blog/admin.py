from django.contrib import admin
from blog.models import Tag, Post, Comment

# customised class to be displayed in admin
class PostAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("title",)}
  list_display = ('slug', 'published_at')

# display in admin
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)