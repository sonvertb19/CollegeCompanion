# Generated by Django 2.2.2 on 2019-07-02 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0002_auto_20190702_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='value_int',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='value_str',
            field=models.CharField(default='Not Marked', max_length=200),
        ),
    ]