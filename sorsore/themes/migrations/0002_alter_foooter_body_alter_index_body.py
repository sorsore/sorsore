# Generated by Django 5.0.9 on 2024-09-11 08:41

import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("themes", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="foooter",
            name="body",
            field=wagtail.fields.StreamField(
                [
                    (
                        "paragraph",
                        wagtail.blocks.StructBlock(
                            [
                                ("title", wagtail.blocks.CharBlock()),
                                ("text", wagtail.blocks.RichTextBlock()),
                            ]
                        ),
                    ),
                    (
                        "link_list",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "title",
                                    wagtail.blocks.CharBlock(required=False),
                                ),
                                (
                                    "links",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.StructBlock(
                                            [
                                                (
                                                    "name",
                                                    wagtail.blocks.CharBlock(),
                                                ),
                                                (
                                                    "page",
                                                    wagtail.blocks.PageChooserBlock(
                                                        label="page",
                                                        required=False,
                                                    ),
                                                ),
                                                (
                                                    "external_url",
                                                    wagtail.blocks.CharBlock(
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
                        "text_list",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "title",
                                    wagtail.blocks.CharBlock(required=False),
                                ),
                                (
                                    "photo",
                                    wagtail.images.blocks.ImageChooserBlock(
                                        required=False
                                    ),
                                ),
                                (
                                    "texts",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.StructBlock(
                                            [
                                                (
                                                    "toggle",
                                                    wagtail.blocks.ChoiceBlock(
                                                        choices=[
                                                            (
                                                                "fa-map-marked-alt",
                                                                "map",
                                                            ),
                                                            (
                                                                "fa-envelope",
                                                                "envelope",
                                                            ),
                                                            (
                                                                "fa-phone-alt",
                                                                "phone",
                                                            ),
                                                        ],
                                                        required=False,
                                                    ),
                                                ),
                                                (
                                                    "image",
                                                    wagtail.images.blocks.ImageChooserBlock(
                                                        required=False
                                                    ),
                                                ),
                                                (
                                                    "text",
                                                    wagtail.blocks.CharBlock(),
                                                ),
                                            ]
                                        )
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "icon_list",
                        wagtail.blocks.StructBlock(
                            [
                                ("title", wagtail.blocks.CharBlock()),
                                (
                                    "icons",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.StructBlock(
                                            [
                                                (
                                                    "icon_name",
                                                    wagtail.blocks.ChoiceBlock(
                                                        choices=[
                                                            (
                                                                "fa-facebook-f",
                                                                "facebook",
                                                            ),
                                                            (
                                                                "fa-twitter",
                                                                "twitter",
                                                            ),
                                                            (
                                                                "fa-instagram",
                                                                "instagram",
                                                            ),
                                                            (
                                                                "fa-pinterest",
                                                                "pinterest",
                                                            ),
                                                        ],
                                                        required=False,
                                                    ),
                                                ),
                                                (
                                                    "other_icon",
                                                    wagtail.blocks.CharBlock(
                                                        required=False
                                                    ),
                                                ),
                                                (
                                                    "external_url",
                                                    wagtail.blocks.URLBlock(
                                                        label="external URL",
                                                        required=False,
                                                    ),
                                                ),
                                            ]
                                        ),
                                        max_num=4,
                                    ),
                                ),
                            ]
                        ),
                    ),
                ],
                use_json_field=True,
            ),
        ),
        migrations.AlterField(
            model_name="index",
            name="body",
            field=wagtail.fields.StreamField(
                [
                    (
                        "carousel",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "image_title",
                                    wagtail.blocks.CharBlock(required=False),
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
                                    wagtail.blocks.CharBlock(required=False),
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
                                                            ("type1", "type1"),
                                                            ("type2", "type2"),
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
                                    wagtail.blocks.CharBlock(required=False),
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
                use_json_field=True,
            ),
        ),
    ]
