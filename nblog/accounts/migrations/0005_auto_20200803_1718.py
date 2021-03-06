# Generated by Django 3.0.8 on 2020-08-03 17:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200803_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(default='1', max_length=15, unique=True, validators=[django.core.validators.RegexValidator(message='Phone number must be entered in the from 9 to 14', regex='^\\+?1?\\d{9,14}$')]),
            preserve_default=False,
        ),
    ]
