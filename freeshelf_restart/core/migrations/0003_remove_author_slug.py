# Generated by Django 2.1.7 on 2019-03-18 07:22
import os.path, csv
from django.conf import settings
from django.core.files import File
from django.db import migrations
from django.utils.text import slugify

def get_book_csv(apps, schema_editor):
    """Read CSV file with book list of ebooks and insert them into DB"""
    Book = apps.get_model('core', 'Book')
    Author = apps.get_model('core', 'Author')
    Topic = apps.get_model('core', 'Topic')
    datapath = os.path.join(settings.BASE_DIR, 'initial_data')
    datafile = os.path.join(datapath, 'initial_books.csv')

    Book.objects.all().delete()
    Topic.objects.all().delete()

    with open(datafile) as file:
        reader = csv.DictReader(file)
        for row in reader:
            book_title = row['title']
            # The following ensures we will not create duplicate books
            if Book.objects.filter(title=book_title).count():
                continue
            # get or create
            author, _ = Author.objects.get_or_create(
                name=row['author'],
            )
            author.save()

            topic, _ = Topic.objects.get_or_create(
                name=row['topic'],
            )
            topic.slug = slugify(topic.name)[:49]
            topic.save()
            
            book = Book(
                title=row['title'],
                author=author,
                description=row['description'],
                book_url=row['book_url'],
                date_added=row['date_added'],
            )

            book.slug = slugify(book.title)[:49]
            book.save()
            book.topics.add(topic)

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190317_2313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='slug',
        ),
    ]
