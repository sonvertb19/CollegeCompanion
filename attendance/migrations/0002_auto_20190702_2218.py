# Generated by Django 2.2.2 on 2019-07-02 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='period',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.Subject'),
        ),
    ]
