# Generated by Django 3.2.6 on 2021-09-05 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snsapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snsmodel',
            name='readtext',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
