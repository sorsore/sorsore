import os

from django.db import models
from django.core.exceptions import ValidationError



class TemplateSettings(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    def clean(self):
        """
        Throw ValidationError if you try to save more than one model instance
        See: http://stackoverflow.com/a/6436008
        """
        model = self.__class__
        if (model.objects.count() > 0 and
                self.id != model.objects.get().id):
            raise ValidationError(
                "Can only create 1 instance of %s." % model.__name__)