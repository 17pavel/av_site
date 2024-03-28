from django.apps import AppConfig


class JobsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'jobs'
    verbose_name ='Рассылки'

    # def ready(self) -> None:
    #     import jobs.signals

