# Generated by Django 4.2.7 on 2023-11-13 17:52

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("mainapp", "0013_user_delete"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="delete",
            new_name="delete_value",
        ),
    ]