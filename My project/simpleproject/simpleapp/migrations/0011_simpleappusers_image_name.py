# Generated by Django 4.1.7 on 2023-03-30 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simpleapp', '0010_remove_simpleappusers_image_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='simpleappusers_image',
            name='name',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
    ]
