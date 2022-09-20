from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class TodosConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "drf_api.todos"
    verbose_name = _("To-Do")
