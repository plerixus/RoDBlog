# Generated by Django 2.0.2 on 2018-03-16 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_remove_article_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
