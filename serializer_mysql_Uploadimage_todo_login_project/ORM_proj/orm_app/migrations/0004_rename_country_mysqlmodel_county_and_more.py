# Generated by Django 4.2.1 on 2023-05-15 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orm_app', '0003_alter_mysqlmodel_web'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mysqlmodel',
            old_name='country',
            new_name='county',
        ),
        migrations.RenameField(
            model_name='mysqlmodel',
            old_name='zip',
            new_name='zip_code',
        ),
    ]
