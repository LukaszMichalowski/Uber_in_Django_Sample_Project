# Generated by Django 3.2.5 on 2022-06-12 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appuber', '0003_destination_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='order_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
