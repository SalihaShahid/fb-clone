# Generated by Django 4.2.3 on 2023-07-25 21:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("facebook_app", "0012_alter_comment_object_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="mediapost",
            name="caption",
            field=models.TextField(default=""),
        ),
    ]
