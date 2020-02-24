# Generated by Django 2.2.8 on 2020-02-24 04:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collaborator', '0005_auto_20200224_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collaborator',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]
