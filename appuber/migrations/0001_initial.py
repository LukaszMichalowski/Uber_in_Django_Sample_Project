# Generated by Django 3.2.5 on 2022-06-12 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255)),
                ('surname', models.CharField(db_index=True, max_length=255)),
                ('slug', models.CharField(db_index=True, max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Client',
            },
        ),
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(db_index=True, max_length=255)),
                ('slug', models.CharField(db_index=True, max_length=255)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destinations', to='appuber.client')),
            ],
            options={
                'verbose_name': 'Destinations',
            },
        ),
    ]
