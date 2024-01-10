# Generated by Django 5.0.1 on 2024-01-09 18:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('role', models.CharField(max_length=20)),
                ('isActive', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Chairman',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('lasttname', models.CharField(max_length=20)),
                ('contact', models.CharField(max_length=11)),
                ('blockno', models.CharField(max_length=3)),
                ('houseno', models.CharField(max_length=4)),
                ('pic', models.FileField(default='default.png', upload_to='media/upload')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
    ]
