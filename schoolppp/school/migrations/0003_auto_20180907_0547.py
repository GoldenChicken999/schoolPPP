# Generated by Django 2.1.1 on 2018-09-07 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_auto_20180907_0545'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schooldata',
            old_name='sid',
            new_name='school_id',
        ),
    ]