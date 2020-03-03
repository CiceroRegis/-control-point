# Generated by Django 2.2.2 on 2020-02-29 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacient', '0010_auto_20200229_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pacient',
            name='medical_record_number',
            field=models.IntegerField(blank=True, default=21975029, editable=False, null=True, verbose_name='Medical record number'),
        ),
        migrations.AlterField(
            model_name='pacient',
            name='photo',
            field=models.ImageField(blank=True, max_length=200, null=True, upload_to='photos'),
        ),
    ]
