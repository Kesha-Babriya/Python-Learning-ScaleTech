from django.apps import AppConfig


class ApiConfig(AppConfig):
    name = 'api'

    def ready(self):
        import api.signals  # સર્વર રન થતાં જ સિગ્નલ એક્ટિવેટ થશે
