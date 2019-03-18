# Generated by Django 2.1.7 on 2019-03-18 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('title', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('description', models.TextField(max_length=1000)),
                ('url', models.URLField(max_length=255, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(unique=True)),
                ('author', models.ManyToManyField(to='core.Author')),
            ],
            options={
                'ordering': ['-date_added'],
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a book topic (e.g. Python)', max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='topic',
            field=models.ManyToManyField(to='core.Topic'),
        ),
    ]
