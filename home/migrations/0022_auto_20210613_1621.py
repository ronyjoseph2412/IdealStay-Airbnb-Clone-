# Generated by Django 3.1.8 on 2021-06-13 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_remove_stayus19_end19'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='stayus19',
            new_name='booktr',
        ),
        migrations.DeleteModel(
            name='turkeybook',
        ),
    ]
