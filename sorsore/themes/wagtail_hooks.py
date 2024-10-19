from django.urls import path, reverse

from wagtail import hooks
from wagtail.admin.panels import FieldPanel
from wagtail.admin.menu import MenuItem, Menu, SubmenuMenuItem
from wagtail.snippets.models import register_snippet
from wagtail.snippets.views.snippets import SnippetViewSet

from .models import Foooter, Index
from .views import new_themes, theme_viewset, settings


# snippets
class FoooterViewSet(SnippetViewSet):
    model = Foooter
    icon = "desktop"
    menu_label = "themes"
    menu_name = "themes"

    panels = [
        FieldPanel("name"),
        FieldPanel("body")
    ]



class IndexViewSet(SnippetViewSet):
    model = Index
    menu_label = "themes"
    menu_name = "themes"
    url_prefix = "themes/homepage"

    panels = [
        FieldPanel("name"),
        FieldPanel("in_use"),
        FieldPanel("body"),
    ]


register_snippet(FoooterViewSet)
register_snippet(IndexViewSet)


# themes settings
@hooks.register('register_admin_urls')
def register_themes_url():
    return[
        path('themes/', settings, name="themes"),
        path('themes/new/', new_themes, name='new'),
        path("themes/homepage/", IndexViewSet, name="homepage"),
    ]

@hooks.register('register_admin_menu_item')
def register_themes_menu_item():
    submenu = Menu(items=[
        MenuItem('settings', reverse('themes'), icon_name='cog'),
        MenuItem('add themes', reverse('new'), icon_name='download'),
        MenuItem('homepage', reverse('homepage'), icon_name='home'),
    ])

    return SubmenuMenuItem('Themes', submenu, icon_name='doc-full')


# @hooks.register("register_admin_viewset")
# def register_viewset():
#     return theme_viewset
