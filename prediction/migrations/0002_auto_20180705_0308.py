# Generated by Django 2.0.5 on 2018-07-05 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prediction', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='classicroutelist',
            name='RouteListName',
            field=models.TextField(default='list name', max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='classicroutelist',
            name='ListAuthor',
            field=models.CharField(max_length=1000),
        ),
    ]
