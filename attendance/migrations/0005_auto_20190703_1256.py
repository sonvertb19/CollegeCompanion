# Generated by Django 2.2.2 on 2019-07-03 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0004_auto_20190703_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='value_int',
            field=models.IntegerField(default=0),
        ),
    ]
