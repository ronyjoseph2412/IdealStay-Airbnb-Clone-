# Generated by Django 3.1.8 on 2021-06-13 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_auto_20210613_1453'),
    ]

    operations = [
        migrations.CreateModel(
            name='bookturkey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstturkey', models.CharField(max_length=122)),
                ('lastturkey', models.CharField(max_length=122)),
                ('emailturkey', models.CharField(max_length=122)),
                ('phoneturkey', models.CharField(max_length=13)),
                ('adultturkey', models.CharField(max_length=13)),
                ('childturkey', models.CharField(max_length=13)),
                ('bookturkey', models.DateField()),
                ('refid', models.IntegerField(default=0, verbose_name='')),
            ],
        ),
    ]
