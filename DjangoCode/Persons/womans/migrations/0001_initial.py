# Generated by Django 2.1.7 on 2019-09-12 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Money',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('number', models.CharField(max_length=25)),
                ('charge', models.IntegerField()),
                ('buy', models.IntegerField()),
                ('mark', models.CharField(max_length=110)),
            ],
        ),
    ]