from django.contrib import admin
from blog.models import Tag, Post

# display in admin as it is
admin.site.register(Tag)

# customised class to be displayed in admin
class PostAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("title",)}
  list_display = ('slug', 'published_at')

admin.site.register(Post, PostAdmin)