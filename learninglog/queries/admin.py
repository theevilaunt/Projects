from django.contrib import admin

# Register your models here.

from queries.models import Blog, Author, Entry

admin.site.register(Blog)
admin.site.register(Author)
admin.site.register(Entry)
