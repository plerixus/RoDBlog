# Generated by Django 2.0.2 on 2018-03-19 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_article_theme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='thumb',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
