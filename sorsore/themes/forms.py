import os

from django import forms
from django.forms.renderers import BaseRenderer
from django.forms.utils import ErrorList

from .models import Index
from django.db.utils import OperationalError

class GetTemplatesForm(forms.Form):
    # TremplateSettings model
    THEMES_LIST = os.listdir(os.getcwd() + "/patterns/templates/patterns")
    THEMES = [(i, i) for i in THEMES_LIST]
    THEMES.insert(0, ("None", "None"))
    template_name = forms.ChoiceField(choices=THEMES)
