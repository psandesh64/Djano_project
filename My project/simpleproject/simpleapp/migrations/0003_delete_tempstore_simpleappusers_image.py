# Generated by Django 4.1.7 on 2023-03-29 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simpleapp', '0002_tempstore'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tempstore',
        ),
        migrations.AddField(
            model_name='simpleappusers',
            name='image',
            field=models.ImageField(default='', upload_to='static/Image/'),
        ),
    ]
