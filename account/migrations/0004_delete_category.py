# Generated by Django 3.2.11 on 2022-02-05 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
    ]
