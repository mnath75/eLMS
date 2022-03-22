# Generated by Django 3.2.11 on 2022-03-22 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='batchCategory',
            fields=[
                ('cat_id', models.AutoField(db_column='cat_id', primary_key=True, serialize=False)),
                ('cat_title', models.CharField(max_length=255, verbose_name='Title')),
                ('cat_slug', models.SlugField(max_length=255, null=True, verbose_name='slug')),
                ('cat_short', models.TextField(blank=True, null=True, verbose_name='short description')),
                ('cat_createddate', models.DateTimeField(auto_now_add=True, verbose_name='created')),
            ],
        ),
    ]