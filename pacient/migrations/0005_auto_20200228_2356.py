# Generated by Django 2.2.2 on 2020-02-29 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacient', '0004_auto_20200228_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pacient',
            name='medical_record_number',
            field=models.IntegerField(default=19219938, editable=False, verbose_name='Medical record number'),
        ),
    ]
