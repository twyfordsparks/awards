from django.apps import AppConfig


class TuzoConfig(AppConfig):
    name = 'tuzo'

    def ready(self):
        import tuzo.signals
