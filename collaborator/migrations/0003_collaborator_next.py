# Generated by Django 2.2.8 on 2020-02-20 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collaborator', '0002_auto_20200218_1343'),
    ]

    operations = [
        migrations.AddField(
            model_name='collaborator',
            name='next',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
