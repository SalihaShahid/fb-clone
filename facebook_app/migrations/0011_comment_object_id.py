# Generated by Django 4.2.3 on 2023-07-25 17:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("facebook_app", "0010_textpost_mediapost_comment"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="object_id",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
