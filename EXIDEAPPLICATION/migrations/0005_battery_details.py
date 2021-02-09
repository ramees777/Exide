# Generated by Django 3.1.5 on 2021-01-05 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EXIDEAPPLICATION', '0004_purchase_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='battery_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bimage', models.FileField(upload_to='')),
                ('bname', models.CharField(max_length=70)),
                ('bdesc', models.CharField(max_length=300)),
                ('vtype', models.CharField(max_length=50)),
                ('ftype', models.CharField(max_length=50)),
                ('bvoltage', models.CharField(max_length=30)),
                ('bprice', models.CharField(max_length=50)),
            ],
        ),
    ]
