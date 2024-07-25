# Generated by Django 5.0.7 on 2024-07-13 18:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('phone_number', models.CharField(max_length=20)),
                ('notes', models.TextField()),
                ('status', models.BooleanField(default=False)),
                ('deliverer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deliverer_services', related_query_name='deliverer_service', to='user.telegramuser')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', related_query_name='service', to='user.telegramuser')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]