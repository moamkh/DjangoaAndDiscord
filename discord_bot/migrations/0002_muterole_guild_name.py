# Generated by Django 5.0.3 on 2024-03-11 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discord_bot', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='muterole',
            name='guild_name',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
    ]