# Generated by Django 3.1.13 on 2021-07-30 20:37

import sorsore.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sorsore', '0020_auto_20210527_1030'),
    ]

    operations = [
        migrations.AddField(
            model_name='analyticssettings',
            name='body_scripts',
            field=sorsore.fields.MonospaceField(blank=True, help_text='Add tracking scripts toward closing <body> tag.', null=True, verbose_name='<body> tracking scripts'),
        ),
        migrations.AddField(
            model_name='analyticssettings',
            name='head_scripts',
            field=sorsore.fields.MonospaceField(blank=True, help_text='Add tracking scripts between the <head> tags.', null=True, verbose_name='<head> tracking scripts'),
        ),
    ]
