# Generated by Django 2.0.2 on 2018-03-18 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_article_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='theme',
            field=models.CharField(choices=[('Gold making', 'Gold making'), ('Dungeons', 'Dungeons'), ('Fractals', 'Fractals'), ('Raids', 'Raids'), ('Builds', 'Builds')], default='Builds', max_length=20),
        ),
    ]