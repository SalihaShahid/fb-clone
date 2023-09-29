# Generated by Django 4.2.3 on 2023-07-25 07:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("facebook_app", "0007_alter_friendrequests_user_email"),
    ]

    operations = [
        migrations.CreateModel(
            name="Message",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("sender", models.EmailField(max_length=254)),
                ("receiver", models.EmailField(max_length=254)),
                ("message", models.TextField()),
                ("time", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
