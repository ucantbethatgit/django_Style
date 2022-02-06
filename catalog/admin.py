from django.contrib import admin

# Register your models here.

from .models import flsAuthor, flsGenre, flsBook, flsBookInstance

admin.site.register(flsBook)
admin.site.register(flsAuthor)
admin.site.register(flsGenre)
admin.site.register(flsBookInstance)
