# Generated by Django 4.2.1 on 2023-05-09 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_remove_review_like_users_review_movie_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='movie_code',
            field=models.IntegerField(),
        ),
    ]