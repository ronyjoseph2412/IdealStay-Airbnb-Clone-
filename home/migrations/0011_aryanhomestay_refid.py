# Generated by Django 3.1.8 on 2021-06-12 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20210613_0119'),
    ]

    operations = [
        migrations.AddField(
            model_name='aryanhomestay',
            name='refid',
            field=models.IntegerField(default=0, verbose_name=''),
        ),
    ]
