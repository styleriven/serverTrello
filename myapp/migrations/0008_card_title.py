# Generated by Django 4.2.1 on 2023-05-04 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_board_owner_alter_token_user_delete_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='title',
            field=models.CharField(default='', max_length=500),
        ),
    ]
