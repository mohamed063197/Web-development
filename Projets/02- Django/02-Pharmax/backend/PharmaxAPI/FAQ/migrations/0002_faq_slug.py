# Generated by Django 5.0 on 2024-01-08 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FAQ', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='faq',
            name='slug',
            field=models.SlugField(default='slug'),
        ),
    ]
