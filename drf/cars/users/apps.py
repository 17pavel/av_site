from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
    verbose_name ='Пользователи телеги'

    def ready(self) -> None:
        import users.signals
