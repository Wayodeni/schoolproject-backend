# Generated by Django 3.1 on 2020-08-10 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_book'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='name',
            new_name='title',
        ),
    ]
