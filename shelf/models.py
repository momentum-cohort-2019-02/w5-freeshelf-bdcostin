from django.db import models
import uuid
from django.urls import reverse

# Create your models here.

class Genre(models.Model):
    '''Model represents the genres'''
    name = models.CharField(max_length=100, help_text='Enter a book genre (e.g. Python)')

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ManyToManyField('Author')
    description = models.TextField(max_length=1000)
    date_added = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular post across whole site')

    def get_absolute_url(self):
        '''Returns the url to access details about the book'''
        return reverse("model_detail", kwargs={"pk": self.pk})
    
    def display_genre(self):
        '''Create a string for the Genre. This is required to display genre in Admin.'''
        return ', '.join(genre.name for genre in self.genre.all()[:3])
    
    def display_author(self):
        '''Create a string for the Genre. This is required to display author in Admin.'''
        return ', '.join(author.name for author in self.author.all()[:3])

    display_author.short_description = 'Genre'

    # class Meta:
    #     ordering = ['date_added']

    def __str__(self):
        return self.title

class Author(models.Model):
    '''Model represents the author(s)'''
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    
    def get_absolute_url(self):
        '''Returns the url to access a particular author instance.'''
        return reverse('author-detail', args=[str(self.id)])

    # class Meta:
    #     order = ['last_name', 'first_name']

    def __str__(self):
        '''String for representing the Model object.'''
        return f'{self.last_name}, {self.first_name}'

