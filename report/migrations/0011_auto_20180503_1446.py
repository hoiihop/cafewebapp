# Generated by Django 2.0.4 on 2018-05-03 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0010_auto_20180503_1159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='f_name',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='l_name',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='position',
        ),
    ]