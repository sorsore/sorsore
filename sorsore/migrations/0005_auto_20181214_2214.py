# Generated by Django 2.0.9 on 2018-12-15 03:14

import sorsore.blocks.base_blocks
import sorsore.fields
from django.db import migrations, models
import django.db.models.deletion
import modelcluster.contrib.taggit
import modelcluster.fields
import wagtail.contrib.table_block.blocks
import wagtail.blocks
import wagtail.fields
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.images.blocks
import wagtail.snippets.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('sorsore', '0004_auto_20181119_1507'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoderedTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='tagged_items', to='sorsore.CoderedPage')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sorsore_coderedtag_items', to='taggit.Tag')),
            ],
            options={
                'verbose_name': 'CodeRed Tag',
            },
        ),
        migrations.AlterField(
            model_name='carouselslide',
            name='content',
            field=sorsore.fields.CoderedStreamField([], blank=True),
        ),
        migrations.AlterField(
            model_name='contentwall',
            name='content',
            field=sorsore.fields.CoderedStreamField([], blank=True, verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='footer',
            name='content',
            field=sorsore.fields.CoderedStreamField([], blank=True, verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='reusablecontent',
            name='content',
            field=sorsore.fields.CoderedStreamField([], blank=True, verbose_name='content'),
        ),
        migrations.AddField(
            model_name='coderedpage',
            name='tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(blank=True, help_text='Used to categorize your pages.', through='sorsore.CoderedTag', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
