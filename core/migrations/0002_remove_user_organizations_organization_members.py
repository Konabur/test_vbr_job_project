# Generated by Django 4.2.7 on 2024-01-16 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='organizations',
        ),
        migrations.AddField(
            model_name='organization',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='organizations', to='core.user'),
        ),
    ]
