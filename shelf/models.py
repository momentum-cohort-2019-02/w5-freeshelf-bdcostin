from django.db import models
import uuid
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils.text import slugify

# Create your models here.

User = get_user_model()

class Topic(models.Model):
    '''Model represents book topics'''
    name = models.CharField(max_length=100, help_text='Enter a book topic (e.g. Python)')
    slug = models.SlugField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.name

class Author(models.Model):
    '''Model represents the author(s)'''
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True, null=True)
    
    def get_absolute_url(self):
        '''Returns the url to access a particular author instance.'''
        return reverse('author-detail', args=[str(self.id)])

    # class Meta:
    #     order = []

    def __str__(self):
        '''String for representing the Model object.'''
        return self.name

class Book(models.Model):
    '''Model represents books'''
    title = models.CharField(max_length=255)
    cover = models.ImageField(upload_to='covers/', null=True, blank=True)

    # Make ManyToMany plural! Will there be another issue here?
    author = models.ManyToManyField(Author)
    description = models.TextField(max_length=1000)
    url = models.URLField(max_length=255, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    # Make ManyToMany plural! Will there be another issue here?
    topic = models.ManyToManyField('Topic', help_text='Select a topic for this book.')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular post across whole site')
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['-date_added']

    def get_absolute_url(self):
        """Returns the url to access a particular book instance."""
        return reverse('book-detail', args=[str(self.slug)])
    
    def display_topic(self):
        '''Create a string for the Topic. This is required to display topic in Admin.'''
        return ', '.join(topic.name for topic in self.topic.all()[:3])
    
    display_topic.short_description = 'Topic'

    def display_author(self):
        '''Create a string for the Topic. This is required to display author in Admin.'''
        return ', '.join(author.name for author in self.author.all()[:2])

    display_author.short_description = 'Author'

# Overrides current save
    def save(self, *args, **kwargs):
        self.set_slug()
        super(Book, self).save(*args, **kwargs)

# If not in database then use as is. 
    def set_slug(self):
        if self.slug:
            return
        base_slug = slugify(self.title)
        slug = base_slug
        n = 0
        while Topic.objects.filter(slug=slug).count():
            n += 1
            slug = base_slug + "-" + str(n)
        self.slug =slug
            
    def __str__(self):
        return self.title

