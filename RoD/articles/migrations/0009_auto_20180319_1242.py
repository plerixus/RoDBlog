# Generated by Django 2.0.2 on 2018-03-19 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_auto_20180319_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='thumb',
            field=models.ImageField(blank=True, default='HEADER.jpg', upload_to=''),
        ),
    ]