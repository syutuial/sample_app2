# Generated by Django 2.2 on 2019-05-05 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='taskname')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='createddate')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='updatedate')),
            ],
        ),
    ]
