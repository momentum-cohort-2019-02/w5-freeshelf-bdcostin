# Generated by Django 2.1.7 on 2019-03-17 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelf', '0012_auto_20190317_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='covers/'),
        ),
    ]