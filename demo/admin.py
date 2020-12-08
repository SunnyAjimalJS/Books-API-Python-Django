from django.contrib import admin
from .models import Book, BookNumber, Character

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    list_filter = ['published']
    search_fields = ['id']


admin.site.register(BookNumber)
admin.site.register(Character)

