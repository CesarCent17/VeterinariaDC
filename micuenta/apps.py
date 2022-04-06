from django.apps import AppConfig


class MicuentaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'micuenta'

    def ready(self):
        from . import signals

        """
            Anula este método en las subclases para ejecutar código cuando se inicia Django. 
        """

