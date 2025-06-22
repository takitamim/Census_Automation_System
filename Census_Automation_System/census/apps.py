from django.apps import AppConfig


class CensusConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "census"

    def ready(self):
        from . import auto_init
        auto_init.initialize()