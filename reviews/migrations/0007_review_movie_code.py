# Generated by Django 4.2.1 on 2023-05-09 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0006_remove_review_movie_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='movie_code',
            field=models.IntegerField(null=True),
        ),
    ]