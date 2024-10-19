from django.db import models

from wagtail.fields import StreamField, RichTextField
from wagtail.models import PreviewableMixin
from wagtail import blocks
from .blocks.index import CarouselBlock, PageCardBlock, OneParagraphBlock, CardListBlock
from wagtail.images.blocks import ImageChooserBlock
from .model_theme import TemplateSettings
# import template_settings as temp


class LinkStructValue(blocks.StructValue):
    def url(self):
        external_url = self.get('external_url')
        page = self.get('page')
        return external_url or page.url
    

class LinkBlock(blocks.StructBlock):
    name =blocks.CharBlock()
    page = blocks.PageChooserBlock(label="page", required=False)
    external_url = blocks.CharBlock( required=False)

    class Meta:
        value_class = LinkStructValue
        template = "themes/blocks/link_block.html"


class IconLinkBlock(blocks.StructBlock):
    icon_name = blocks.ChoiceBlock(choices=[
        ('fa-facebook-f', "facebook"),
        ('fa-twitter', 'twitter'),
        ('fa-instagram', 'instagram'),
        ('fa-pinterest', 'pinterest')
    ], required=False)
    other_icon = blocks.CharBlock(required=False)
    external_url = blocks.URLBlock(label="external URL", required=False)

    class Meta:
        value_class = LinkStructValue
        template = "themes/blocks/icon_block.html"


class ToggleBlock(blocks.StructBlock):
    toggle =  blocks.ChoiceBlock(choices=[
                ("fa-map-marked-alt", "map"),
                ("fa-envelope", "envelope"),
                ("fa-phone-alt", "phone"),
        ], required=False)
    image = ImageChooserBlock(required=False)
    text = blocks.CharBlock()
    
    class Meta:
        template ="themes/blocks/toggle.html"



class Foooter(models.Model):
    name = models.CharField(max_length=100)
    body = StreamField([
        ("paragraph", blocks.StructBlock([
            ("title", blocks.CharBlock()),
            ("text", blocks.RichTextBlock())
        ])),
        ("link_list", blocks.StructBlock([
            ("title", blocks.CharBlock(required=False)),
            ("links", blocks.ListBlock(LinkBlock()))
        ])),
        ("text_list", blocks.StructBlock([
            ("title", blocks.CharBlock(required=False)),
            ("photo", ImageChooserBlock(required=False)), 
            ("texts", blocks.ListBlock(ToggleBlock()))
            
        ])),
        ("icon_list", blocks.StructBlock([
            ("title", blocks.CharBlock()),
            ("icons", blocks.ListBlock(IconLinkBlock(), max_num=4))
        ]))
    ], use_json_field=True, max_num=4,)

    def __str__(self):

        return self.name
    

# class Index(models.Model):
#     body = StreamField([
#         ("carousel", )
#     ], use_json_field=True)

class Index(PreviewableMixin, models.Model):
    name = models.CharField(max_length=100, default="index")
    in_use = models.BooleanField(default=False)
    body = StreamField([
        ("carousel", CarouselBlock()),
        ("page_card_list", PageCardBlock()),
        ("card_list", CardListBlock()),
        ("one_paragraph", OneParagraphBlock()),
    ], use_json_field=True)

    def get_preview_template(self, request, mode_name):
        return "themes/previews/index.html"
    
    def __str__(self):
        return self.name



    
    