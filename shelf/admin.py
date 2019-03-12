from django.contrib import admin
from shelf.models import Author, Book, Topic

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_author', 'display_topic')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    display = 'display_name'

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    display = 'display_topic'
