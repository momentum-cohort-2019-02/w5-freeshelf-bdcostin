from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth import get_user_model


# Create your models here.

User = get_user_model()

class Topic(models.Model):
    '''Model represents the authors'''
    name = models.CharField(max_length=255, help_text='Enter a book topic (e.g. Python)',  null=True, blank=True)
    slug = models.SlugField()
    

    def __str__(self):
        return self.name

class Author(models.Model):
    '''Model represents the authors'''
    name = models.CharField(max_length=255, null=True)
    
    # String representation of model
    def __str__(self):
        return self.name

class Book(models.Model):
    '''Model represents the available books'''
    title = models.CharField(max_length=255, primary_key=True)
    author = models.ManyToManyField(Author)
    topic = models.ManyToManyField(Topic)
    description = models.TextField(max_length=1000)
    url = models.URLField(max_length=255, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)
    # favorited_by = models.ManyToManyField(to=User,related_name="favorite_books", blank=True)

    class Meta:
        ordering = ['-date_added']

    def display_topic(self):
        '''Create a string for the Topic. This is required to display topic in Admin.'''
        return ', '.join(topic.name for topic in self.topic.all()[:3])
    
    display_topic.short_description = 'Topic'

    def display_author(self):
        '''Create a string for the Topic. This is required to display author in Admin.'''
        return ', '.join(author.name for author in self.author.all()[:2])

    display_author.short_description = 'Author'
    
    def set_slug(self):
        """Setting slug field to auto-generate and make unique each time even if title is same title as another book-- it will add int at end if needed"""
        if self.slug:
            return
        base_slug = slugify(self.title)
        # Local variable slug below
        slug = base_slug
        n = 0
       
        while Book.objects.filter(slug=slug).count():
            n += 1
            slug = base_slug + "-" + str(n)

        self.slug = slug

    def save(self, *args, **kwargs):
        '''Hides slug field in admin'''
        self.set_slug()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        '''Returns the url to access particular instance of Book model'''
        return reverse('book-detail', args=[str(self.slug)])
    
    # String representation of model
    def __str__(self):
        return self.title

