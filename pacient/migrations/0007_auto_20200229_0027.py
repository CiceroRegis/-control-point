# Generated by Django 2.2.2 on 2020-02-29 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacient', '0006_auto_20200229_0014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pacient',
            name='medical_record_number',
            field=models.IntegerField(blank=True, default=-15053620, editable=False, null=True, verbose_name='Medical record number'),
        ),
    ]