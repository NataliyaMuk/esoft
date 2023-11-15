# Generated by Django 4.2.5 on 2023-11-15 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0015_alter_realestate_latitude_alter_realestate_longitude'),
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('region_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='realestate',
            name='latX',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='realestate',
            name='lngY',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='realestate',
            name='region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='regionRealEstate', to='mainapp.region'),
        ),
    ]