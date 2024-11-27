from django.apps import AppConfig


class ArticleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'article'

class CapitalsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'capitals'