# Generated by Django 2.1.7 on 2019-03-13 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelf', '0008_book_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
