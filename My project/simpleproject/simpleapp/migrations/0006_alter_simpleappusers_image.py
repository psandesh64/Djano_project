# Generated by Django 4.1.7 on 2023-03-29 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simpleapp', '0005_alter_simpleappusers_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='simpleappusers',
            name='image',
            field=models.ImageField(default=None, null=True, upload_to='images/'),
        ),
    ]
