# Generated by Django 4.2.3 on 2023-07-24 10:41

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("facebook_app", "0005_alter_user_password_friendrequests"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="friendrequests",
            unique_together={("user_email", "friend_email")},
        ),
    ]
