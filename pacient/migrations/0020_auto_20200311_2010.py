# Generated by Django 2.2.2 on 2020-03-11 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacient', '0019_auto_20200311_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pacient',
            name='medical_record_number',
            field=models.IntegerField(blank=True, default=7506684, editable=False, null=True, verbose_name='Medical record number'),
        ),
    ]
