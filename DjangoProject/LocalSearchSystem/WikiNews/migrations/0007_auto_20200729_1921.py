# Generated by Django 3.0.8 on 2020-07-30 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WikiNews', '0006_wikinewsitem_lastupdated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wikinewsitem',
            name='image',
            field=models.CharField(max_length=1000),
        ),
    ]
