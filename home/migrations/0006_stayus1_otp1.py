# Generated by Django 3.1.8 on 2021-06-09 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_stayus2_stayus3'),
    ]

    operations = [
        migrations.AddField(
            model_name='stayus1',
            name='otp1',
            field=models.CharField(default='', max_length=5),
        ),
    ]
