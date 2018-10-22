from django.contrib import admin

from .models import Article, Author

admin.site.register(Author)
admin.site.register(Article)
