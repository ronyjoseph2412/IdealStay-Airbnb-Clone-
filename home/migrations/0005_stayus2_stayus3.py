# Generated by Django 3.1.8 on 2021-06-08 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20210604_2118'),
    ]

    operations = [
        migrations.CreateModel(
            name='stayus2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname2', models.CharField(max_length=122)),
                ('lastname2', models.CharField(max_length=122)),
                ('email2', models.CharField(max_length=122)),
                ('phone2', models.CharField(max_length=13)),
                ('adult2', models.CharField(max_length=13)),
                ('child2', models.CharField(max_length=13)),
                ('start2', models.DateField()),
                ('end2', models.DateField()),
                ('address2', models.TextField()),
                ('state2', models.CharField(max_length=13)),
                ('pin2', models.CharField(max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='stayus3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname3', models.CharField(max_length=122)),
                ('lastname3', models.CharField(max_length=122)),
                ('email3', models.CharField(max_length=122)),
                ('phone3', models.CharField(max_length=13)),
                ('adult3', models.CharField(max_length=13)),
                ('child3', models.CharField(max_length=13)),
                ('start3', models.DateField()),
                ('end3', models.DateField()),
                ('address3', models.TextField()),
                ('state3', models.CharField(max_length=13)),
                ('pin3', models.CharField(max_length=7)),
            ],
        ),
    ]
