# Generated by Django 3.2.3 on 2021-05-18 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0004_item_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='priority',
            field=models.TextField(default=''),
        ),
    ]
