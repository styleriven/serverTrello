# Generated by Django 4.2.1 on 2023-05-04 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_card_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='list',
            old_name='name',
            new_name='title',
        ),
    ]
