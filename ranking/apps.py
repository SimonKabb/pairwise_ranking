from django.apps import AppConfig


class RankingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ranking'

    def ready(self):
        import ranking.signals  # Импорт файла с сигналами
