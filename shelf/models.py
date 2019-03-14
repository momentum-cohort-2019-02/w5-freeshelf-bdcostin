from django.db import models
import uuid
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Topic(models.Model):
    '''Model represents book topics'''
    name = models.CharField(max_length=100, help_text='Enter a book topic (e.g. Python)')

    def __str__(self):
        return self.name

class Book(models.Model):
    '''Model represents books'''
    title = models.CharField(max_length=255)
    cover = models.ImageField(upload_to='covers/', null=True)
    author = models.ManyToManyField('Author')
    description = models.TextField(max_length=1000)
    url = models.URLField(max_length=255, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    topic = models.ManyToManyField('Topic', help_text='Select a topic for this book.')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular post across whole site')
    slug = models.SlugField(unique=True)

    def get_absolute_url(self):
        '''Returns the url to access details about the book'''
        return reverse("model_detail", kwargs={"pk": self.pk})
    
    def display_topic(self):
        '''Create a string for the Topic. This is required to display topic in Admin.'''
        return ', '.join(topic.name for topic in self.topic.all()[:3])
    
    display_topic.short_description = 'Topic'

    def display_author(self):
        '''Create a string for the Topic. This is required to display author in Admin.'''
        return ', '.join(author.name for author in self.author.all()[:2])

    display_author.short_description = 'Author'

    class Meta:
        ordering = ['-date_added']

# Overrides current save
    def save(self, *args, **kwargs):
        self.set_slug()
        super().save(*args, **kwargs)

# If not in database then use as is. 
    def set_slug(self):
        if self.slug:
            return
            
    def __str__(self):
        return self.title

class Author(models.Model):
    '''Model represents the author(s)'''
    name = models.CharField(max_length=100)
    # first_name = models.CharField(max_length=100)
    # last_name = models.CharField(max_length=100)
    
    def get_absolute_url(self):
        '''Returns the url to access a particular author instance.'''
        return reverse('author-detail', args=[str(self.id)])

    # class Meta:
    #     order = []

    def __str__(self):
        '''String for representing the Model object.'''
        return self.name
