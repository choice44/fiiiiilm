# Generated by Django 4.2.1 on 2023-05-09 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_review_like_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='like_users',
        ),
        migrations.AddField(
            model_name='review',
            name='movie_code',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]