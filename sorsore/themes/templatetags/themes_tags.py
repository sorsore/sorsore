from django import template

from sorsore.themes.models import Foooter, Index
from sorsore.themes.model_theme import TemplateSettings as Theme

register = template.Library()

# ...

# Foter snippets
@register.inclusion_tag('themes/tags/foters.html', takes_context=True)
def foters(context):
    theme = Theme.objects.first()
    return {
        'foter': Foooter.objects.all(),
        'footer_context': f"patterns/{theme}/footer.html",
        'request': context['request'],
    }


# Index snippets
@register.inclusion_tag('themes/tags/index.html', takes_context=True)
def Indexes(context):
    return {
        'index': Index.objects.all(),
        'request': context['request'],
    }


@register.filter()
def cut(string, part=0):
    num = len(string)
    if num >= 2:
        if part == 0:
            return string[:num//2]
        return string[num//2:]
    else:
        return string
    

@register.filter(name="index_num")
def index(mylist, item):
    if item in mylist:
        return mylist.index(item)
    

@register.filter()
def length(mylist):
    return len(mylist) -1

@register.filter()
def aaa(mylist):
    if len(mylist) > 1:
        return [mylist[len(mylist)-1], mylist[:len(mylist)-1]]
    else:
        return[mylist, mylist]


# Navbar context
@register.filter()
def nav_context(strig):
    theme = Theme.objects.first()
    return f"patterns/{theme}/navbar.html"


@register.simple_tag()
def theme_type():
    theme = Theme.objects.first()
    if theme:
        return theme.name
    else:
        return 'None'