from django.apps import AppConfig


class sorsoreConfig(AppConfig):
    name = "sorsore"
    verbose_name = "Wagtail CRX"
    # TODO: At some point in the future, change this to BigAutoField and create
    # the corresponding migration for concrete models in sorsore.
    default_auto_field = "django.db.models.AutoField"
