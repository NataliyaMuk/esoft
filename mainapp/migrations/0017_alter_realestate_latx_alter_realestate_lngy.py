# Generated by Django 4.2.5 on 2023-11-15 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0016_region_realestate_latx_realestate_lngy_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realestate',
            name='latX',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='realestate',
            name='lngY',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
