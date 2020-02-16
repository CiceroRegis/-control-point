# Generated by Django 2.2.8 on 2020-02-16 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collaborator', '0003_auto_20191226_1733'),
    ]

    operations = [
        migrations.AddField(
            model_name='collaborator',
            name='landline',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='landline'),
        ),
        migrations.AddField(
            model_name='collaborator',
            name='phone_number',
            field=models.CharField(max_length=15, null=True, verbose_name='phone number'),
        ),
        migrations.AddField(
            model_name='collaborator',
            name='sexo',
            field=models.CharField(blank=True, choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='collaborator',
            name='birth',
            field=models.DateField(blank=True, null=True, verbose_name='date of birth'),
        ),
    ]
