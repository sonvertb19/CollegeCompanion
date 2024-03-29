# Generated by Django 2.2.2 on 2019-07-02 08:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('percentage', models.FloatField(blank=True, default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField()),
                ('day', models.PositiveIntegerField()),
                ('venue', models.CharField(default='---', max_length=200)),
                ('period_number', models.PositiveIntegerField()),
                ('subject', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='attendance.Subject')),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('value_int', models.IntegerField(default=-1)),
                ('value_str', models.CharField(max_length=200)),
                ('period', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.Period')),
            ],
        ),
    ]
