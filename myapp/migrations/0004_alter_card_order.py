# Generated by Django 4.1.7 on 2023-04-19 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0003_alter_card_description_alter_card_order"),
    ]

    operations = [
        migrations.AlterField(
            model_name="card",
            name="order",
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
