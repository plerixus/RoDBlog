# Generated by Django 2.0.2 on 2018-03-16 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_article_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='slug',
        ),
    ]
