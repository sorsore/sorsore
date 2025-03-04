# Generated by Django 5.0.9 on 2024-09-11 08:50

import django.db.models.deletion
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sorsore", "0040_remove_analyticssettings_ga_tracking_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="LandingPage",
            fields=[
                (
                    "coderedpage_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="sorsore.coderedpage",
                    ),
                ),
                (
                    "body",
                    wagtail.fields.StreamField(
                        [
                            (
                                "carousel",
                                wagtail.blocks.StructBlock(
                                    [
                                        (
                                            "image_title",
                                            wagtail.blocks.CharBlock(
                                                required=False
                                            ),
                                        ),
                                        (
                                            "image",
                                            wagtail.images.blocks.ImageChooserBlock(
                                                required=False
                                            ),
                                        ),
                                        (
                                            "slides",
                                            wagtail.blocks.ListBlock(
                                                wagtail.blocks.StructBlock(
                                                    [
                                                        (
                                                            "photo",
                                                            wagtail.images.blocks.ImageChooserBlock(
                                                                required=False
                                                            ),
                                                        ),
                                                        (
                                                            "text",
                                                            wagtail.blocks.ListBlock(
                                                                wagtail.blocks.StructBlock(
                                                                    [
                                                                        (
                                                                            "text",
                                                                            wagtail.blocks.CharBlock(
                                                                                label="title"
                                                                            ),
                                                                        ),
                                                                        (
                                                                            "kind",
                                                                            wagtail.blocks.ChoiceBlock(
                                                                                choices=[
                                                                                    (
                                                                                        "h1",
                                                                                        "h1",
                                                                                    ),
                                                                                    (
                                                                                        "h2",
                                                                                        "h2",
                                                                                    ),
                                                                                ]
                                                                            ),
                                                                        ),
                                                                    ]
                                                                ),
                                                                max_num=2,
                                                            ),
                                                        ),
                                                        (
                                                            "button_text",
                                                            wagtail.blocks.ListBlock(
                                                                wagtail.blocks.CharBlock(
                                                                    label="text of button"
                                                                ),
                                                                max_num=1,
                                                            ),
                                                        ),
                                                        (
                                                            "page",
                                                            wagtail.blocks.PageChooserBlock(
                                                                label="page"
                                                            ),
                                                        ),
                                                        (
                                                            "is_active",
                                                            wagtail.blocks.BooleanBlock(
                                                                required=False
                                                            ),
                                                        ),
                                                    ]
                                                )
                                            ),
                                        ),
                                    ]
                                ),
                            ),
                            (
                                "page_card_list",
                                wagtail.blocks.StructBlock(
                                    [
                                        ("title", wagtail.blocks.CharBlock()),
                                        (
                                            "image",
                                            wagtail.images.blocks.ImageChooserBlock(
                                                required=False
                                            ),
                                        ),
                                        (
                                            "page_type",
                                            wagtail.blocks.PageChooserBlock(
                                                label="index page"
                                            ),
                                        ),
                                        (
                                            "num_posts",
                                            wagtail.blocks.IntegerBlock(
                                                default=3,
                                                label="number of pages to show",
                                            ),
                                        ),
                                        (
                                            "card_type",
                                            wagtail.blocks.ChoiceBlock(
                                                choices=[
                                                    ("type1", "type1"),
                                                    ("type2", "type2"),
                                                ],
                                                label="card type",
                                            ),
                                        ),
                                        (
                                            "button_text",
                                            wagtail.blocks.CharBlock(
                                                default="more", required=False
                                            ),
                                        ),
                                    ]
                                ),
                            ),
                            (
                                "card_list",
                                wagtail.blocks.StructBlock(
                                    [
                                        (
                                            "title",
                                            wagtail.blocks.CharBlock(
                                                required=False
                                            ),
                                        ),
                                        (
                                            "image",
                                            wagtail.images.blocks.ImageChooserBlock(
                                                required=False
                                            ),
                                        ),
                                        (
                                            "coverImage",
                                            wagtail.blocks.BooleanBlock(
                                                label="image cover section or not",
                                                required=False,
                                            ),
                                        ),
                                        (
                                            "list_type",
                                            wagtail.blocks.ChoiceBlock(
                                                choices=[
                                                    ("type1", "type1"),
                                                    ("type2", "type2"),
                                                ],
                                                label="list type",
                                            ),
                                        ),
                                        (
                                            "cards",
                                            wagtail.blocks.ListBlock(
                                                wagtail.blocks.StructBlock(
                                                    [
                                                        (
                                                            "title",
                                                            wagtail.blocks.CharBlock(
                                                                required=False
                                                            ),
                                                        ),
                                                        (
                                                            "photo",
                                                            wagtail.images.blocks.ImageChooserBlock(
                                                                required=False
                                                            ),
                                                        ),
                                                        (
                                                            "text",
                                                            wagtail.blocks.RichTextBlock(
                                                                required=False
                                                            ),
                                                        ),
                                                        (
                                                            "icon",
                                                            wagtail.blocks.CharBlock(
                                                                label="icon bootstrap name",
                                                                required=False,
                                                            ),
                                                        ),
                                                        (
                                                            "page",
                                                            wagtail.blocks.PageChooserBlock(
                                                                required=False
                                                            ),
                                                        ),
                                                        (
                                                            "button_text",
                                                            wagtail.blocks.CharBlock(
                                                                required=False
                                                            ),
                                                        ),
                                                        (
                                                            "card_type",
                                                            wagtail.blocks.ChoiceBlock(
                                                                choices=[
                                                                    (
                                                                        "type1",
                                                                        "type1",
                                                                    ),
                                                                    (
                                                                        "type2",
                                                                        "type2",
                                                                    ),
                                                                ],
                                                                label="card type",
                                                            ),
                                                        ),
                                                    ]
                                                )
                                            ),
                                        ),
                                    ]
                                ),
                            ),
                            (
                                "one_paragraph",
                                wagtail.blocks.StructBlock(
                                    [
                                        (
                                            "title",
                                            wagtail.blocks.CharBlock(
                                                required=False
                                            ),
                                        ),
                                        (
                                            "image",
                                            wagtail.images.blocks.ImageChooserBlock(
                                                required=False
                                            ),
                                        ),
                                        (
                                            "section_type",
                                            wagtail.blocks.ChoiceBlock(
                                                choices=[
                                                    ("type1", "type1"),
                                                    ("type2", "type2"),
                                                ],
                                                label="section type",
                                            ),
                                        ),
                                        (
                                            "paragraph",
                                            wagtail.blocks.RichTextBlock(
                                                required=False
                                            ),
                                        ),
                                        (
                                            "link",
                                            wagtail.blocks.ListBlock(
                                                wagtail.blocks.StructBlock(
                                                    [
                                                        (
                                                            "text",
                                                            wagtail.blocks.CharBlock(
                                                                required=False
                                                            ),
                                                        ),
                                                        (
                                                            "page",
                                                            wagtail.blocks.PageChooserBlock(
                                                                required=False
                                                            ),
                                                        ),
                                                        (
                                                            "external_url",
                                                            wagtail.blocks.URLBlock(
                                                                required=False
                                                            ),
                                                        ),
                                                    ]
                                                )
                                            ),
                                        ),
                                    ]
                                ),
                            ),
                        ],
                        blank=True,
                        null=True,
                        use_json_field=True,
                        verbose_name="themes body",
                    ),
                ),
            ],
            options={
                "verbose_name": "Landing Page",
            },
            bases=("sorsore.coderedpage",),
        ),
    ]
