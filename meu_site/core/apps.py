from django.apps import AppConfig

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    # Ligar os espiões de segurança (Logs)
    def ready(self):
        import core.signals