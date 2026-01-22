from django.apps import AppConfig


class CatalogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'catalog'

    def ready(self):
        # Import project-level signals so they are registered when Django starts.
        # Wrapping in try/except prevents breaking management commands if import fails.
        try:
            import product_hub.signals  # noqa: F401
        except Exception:
            pass