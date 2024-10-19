import logging

from wagtail.fields import StreamField, RichTextField
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock

# from sorsore.blocks.base_blocks import ClassifierTermChooserBlock

from sorsore.themes.model_theme import TemplateSettings as Theme
from sorsore.themes.template_settings import *


logger = logging.getLogger("sorsore")


class LinkStructValue(blocks.StructValue):
    def url(self):
        external_url = self.get('external_url')
        page = self.get('page')
        return external_url or page.url
    

# ---------------------------------------------------------
# carousel
# ----------------------------------------------------------
class SlideTextkind(blocks.StructBlock):
    text = blocks.CharBlock(label=CAROUSEL["text1"])
    kind = blocks.ChoiceBlock(CAROUSEL["text_types"])

class SlideCarousel(blocks.StructBlock):
    photo = ImageChooserBlock(required=False)
    
    text = blocks.ListBlock(SlideTextkind(), max_num=CAROUSEL["n_text"])

    button_text = blocks.ListBlock(blocks.CharBlock(label=CAROUSEL["t_button"]), max_num=CAROUSEL["n_button"])

    page = blocks.PageChooserBlock(label="page")

    is_active = blocks.BooleanBlock(required=False)

    class Meta:
        value_class = LinkStructValue


class CarouselBlock(blocks.StructBlock):
    image_title = blocks.CharBlock(required=False)
    image = ImageChooserBlock(required=False)
    slides = blocks.ListBlock(SlideCarousel())

    class Meta:
        template = "themes/blocks/carousel.html"
        

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        theme = Theme.objects.first()


        if theme:
            context["carousel_context"] = f"patterns/{theme}/carousel.html"
        else:
            context["carousel_context"] = f"patterns/theme1/carousel.html"
        
        return context


# ----------------------------------------------------------
# Page Card List
# ----------------------------------------------------------
class PageCardLinkStructValue(blocks.StructValue):
    def url(self):
        external_url = self.get('external_url')
        page = self.get('page_type')
        return external_url or page.url
    
class PageCardBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    image = ImageChooserBlock(required=False)
    page_type = blocks.PageChooserBlock(label="index page")
    num_posts = blocks.IntegerBlock(default=3, label="number of pages to show")
    card_type = blocks.ChoiceBlock(choices=PAGE_LIST["types"], label="card type", default=PAGE_LIST["types"][0])
    button_text = blocks.CharBlock(required=False, default="more")

    class Meta:
        value_class = PageCardLinkStructValue
        template = "themes/blocks/card_page.html"

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)

        indexer = value["page_type"].specific
        # try to use the CoderedPage `get_index_children()`,
        # but fall back to get_children if this is a non-CoderedPage
        if hasattr(indexer, "get_index_children"):
            pages = indexer.get_index_children()
            # if value["classified_by"]:
            #     try:
            #         pages = pages.filter(
            #             classifier_terms=value["classified_by"]
            #         )
            #     except AttributeError:
            #         # `pages` is not a queryset, or is not a queryset of CoderedPage.
            #         logger.warning(
            #             (
            #                 "Tried to filter by ClassifierTerm in PageListBlock, "
            #                 "but <%s.%s ('%s')>.get_index_children() "
            #                 "did not return a queryset or is not a queryset of "
            #                 "CoderedPage models."
            #             ),
            #             indexer._meta.app_label,
            #             indexer.__class__.__name__,
            #             indexer.title,
            #         )
        else:
            pages = indexer.get_children().live()
        
        all_pages = len(pages)
        print(all_pages, value["num_posts"])
        if value["num_posts"] <= all_pages:
            context["pages"] = pages[(all_pages - value["num_posts"]):]
        else:
            context["pages"] = pages[:]

        theme = Theme.objects.first()

        if theme:
            context["card_page_context"] = f"patterns/{theme}/card_page.html"
        else:
            context["card_page_context"] = f"patterns/theme1/card_page.html"
        
        return context
    

# ------------------------------------------------------------
# Card List
# ------------------------------------------------------------
class CardBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False)
    photo = ImageChooserBlock(required=False)
    text = blocks.RichTextBlock(required=False)
    icon = blocks.CharBlock(required=False, label="icon bootstrap name")
    page = blocks.PageChooserBlock(required=False)
    button_text = blocks.CharBlock(required=False)
    card_type = blocks.ChoiceBlock(choices=CARD_LIST["card_type"], label="card type", default=CARD_LIST["card_type"][0])

    class Meta:
        value_class = LinkStructValue
        template = "themes/blocks/card.html"

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        theme = Theme.objects.first()

        if theme:
            context["card_context"] = f"patterns/{theme}/card.html"
        else:
            context["card_context"] = f"patterns/theme1/card.html"
        
        return context



class CardListBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False)
    image = ImageChooserBlock(required=False)
    coverImage = blocks.BooleanBlock(required=False, label="image cover section or not")
    list_type = blocks.ChoiceBlock(choices=CARD_LIST["list_type"], label="list type", default=CARD_LIST["list_type"][0])
    cards = blocks.ListBlock(CardBlock())
    

    class Meta:
        template = "themes/blocks/card_list.html"

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        theme = Theme.objects.first()

        if theme:
            context["card_list_context"] = f"patterns/{theme}/card_list.html"
        else:
            context["card_list_context"] = f"patterns/theme1/card_list.html"
        
        return context


# ------------------------------------------------------------
# One Paragraph
# ------------------------------------------------------------
class OneParagraphButton(blocks.StructBlock):
    text = blocks.CharBlock(required=False)
    page = blocks.PageChooserBlock(required=False)
    external_url = blocks.URLBlock(required=False)

    class Meta:
        value_class = LinkStructValue

class OneParagraphBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False)
    image = ImageChooserBlock(required=False)
    section_type = blocks.ChoiceBlock(choices=ONE_PARAGRAPH["section_type"], label="section type", default=ONE_PARAGRAPH["section_type"][0])
    paragraph = blocks.RichTextBlock(required=False)
    link = blocks.ListBlock(OneParagraphButton())

    class Meta:
        template = "themes/blocks/one_paragraph.html"

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        theme = Theme.objects.first()

        if theme:
            context["one_paragraph_context"] = f"patterns/{theme}/one_paragraph.html"
        else:
            context["one_paragraph_context"] = f"patterns/theme1/one_paragraph.html"
        
        return context



    


