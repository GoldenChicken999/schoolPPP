# Generated by Django 2.1.1 on 2018-09-07 12:43

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
                ('sid', models.IntegerField(max_length=100)),
                ('ele_k', models.IntegerField(max_length=100)),
                ('ele_u', models.IntegerField(max_length=100)),
                ('hea_k', models.IntegerField(max_length=100)),
                ('hea_u', models.IntegerField(max_length=100)),
                ('wat_l', models.IntegerField(max_length=100)),
                ('wat_u', models.IntegerField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Schools',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('saddress', models.CharField(max_length=100)),
                ('semail', models.EmailField(max_length=100)),
            ],
        ),
    ]
