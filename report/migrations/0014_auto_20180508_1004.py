# Generated by Django 2.0.5 on 2018-05-08 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0013_remove_document_edit_flag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentlines',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
        ),
    ]
