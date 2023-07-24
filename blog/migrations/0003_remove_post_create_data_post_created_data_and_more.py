# Generated by Django 4.2.3 on 2023-07-21 20:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_comments_create_date_comments_created_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='create_data',
        ),
        migrations.AddField(
            model_name='post',
            name='created_data',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 21, 20, 14, 5, 766161, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='comments',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 21, 20, 14, 5, 767220, tzinfo=datetime.timezone.utc)),
        ),
    ]
