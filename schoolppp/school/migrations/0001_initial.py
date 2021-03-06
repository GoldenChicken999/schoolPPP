# Generated by Django 2.1.1 on 2018-09-09 00:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True
    dependencies = [
    ]
    operations = [
        migrations.CreateModel(
            name='SchoolData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_id', models.IntegerField()),
                ('year', models.IntegerField()),
                ('month', models.IntegerField()),
                ('week', models.IntegerField()),
                ('ele_k', models.IntegerField()),
                ('ele_u', models.IntegerField()),
                ('hea_k', models.IntegerField()),
                ('hea_u', models.IntegerField()),
                ('wat_l', models.IntegerField()),
                ('wat_u', models.IntegerField()),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
            options={
                'db_table': 'school_schooldata',
            },
        ),
        migrations.CreateModel(
            name='Schools',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
            options={
                'db_table': 'school_schools',
            },
        ),
    ]
