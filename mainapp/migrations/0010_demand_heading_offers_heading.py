# Generated by Django 4.2.7 on 2023-11-12 08:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mainapp", "0009_demand"),
    ]

    operations = [
        migrations.AddField(
            model_name="demand",
            name="heading",
            field=models.CharField(default=1, max_length=255),
        ),
        migrations.AddField(
            model_name="offers",
            name="heading",
            field=models.CharField(default=1, max_length=255),
        ),
    ]
