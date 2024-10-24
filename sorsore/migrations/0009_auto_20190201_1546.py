# Generated by Django 2.1.5 on 2019-02-01 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sorsore', '0008_auto_20190122_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coderedpage',
            name='index_order_by',
            field=models.CharField(blank=True, choices=[('', 'Default Ordering'), ('-first_published_at', 'Date first published, newest to oldest'), ('first_published_at', 'Date first published, oldest to newest'), ('-last_published_at', 'Date updated, newest to oldest'), ('last_published_at', 'Date updated, oldest to newest'), ('title', 'Title, alphabetical'), ('-title', 'Title, reverse alphabetical')], default='', max_length=255, verbose_name='Order child pages by'),
        ),
    ]
