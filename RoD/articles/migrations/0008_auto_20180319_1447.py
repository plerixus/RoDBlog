# Generated by Django 2.0.2 on 2018-03-19 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_auto_20180319_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='thumb',
            field=models.ImageField(blank=True, default='HADER.JPG', upload_to=''),
        ),
    ]
