# Generated by Django 3.2.11 on 2022-01-27 05:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='isbn',
            new_name='bookId',
        ),
    ]
