# Generated by Django 4.2.5 on 2023-11-05 22:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mainapp", "0002_user_nickname_alter_user_email_alter_user_is_realtor"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="Active",
            field=models.SmallIntegerField(null=True),
        ),
    ]
