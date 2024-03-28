
import logging
from django.conf import settings
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
from django_apscheduler import util

from scheduled_tasks import schedule_jobs, schedule_jobs_date, schedule_jobs_last_message, schedule_jobs_first_message

logger = logging.getLogger(__name__)

# The `close_old_connections` decorator ensures that database connections, that have become
# unusable or are obsolete, are closed before and after your job has run. You should use it
# to wrap any jobs that you schedule that access the Django database in any way. 
@util.close_old_connections
def delete_old_job_executions(max_age=604_800):
    """
    This job deletes APScheduler job execution entries older than `max_age` from the database.
    It helps to prevent the database from filling up with old historical records that are no
    longer useful.

    :param max_age: The maximum length of time to retain historical job execution records.
                    Defaults to 7 days.
    """
    DjangoJobExecution.objects.delete_old_job_executions(max_age)


def my_job_minute():
    jobs = temp.filter(triger="minute")
    schedule_jobs(jobs)


def my_job_second():
    jobs = temp.filter(triger="second")
    schedule_jobs_date(jobs)

def my_job_last():
    jobs = temp.filter(triger="last")
    schedule_jobs_last_message(jobs)

def my_job_first():
    jobs = temp.filter(triger="first")
    schedule_jobs_first_message(jobs)

class Triger(BaseCommand):
    help = "Runs APScheduler."

    def handle(self, jobs, *args, **options):
        global temp
        temp = jobs
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")
        try:
            scheduler.add_job(
                my_job_minute,
                next_run_time=jobs.filter(triger='minute')[0].date_create,
                trigger=CronTrigger(minute=f"*/{jobs.filter(triger='minute')[0].period}"),
                id="my_job_minute",  # The `id` assigned to each job MUST be unique
                max_instances=11,
                replace_existing=True,
            )
        except Exception as e:

            print(e)

        try:
            scheduler.add_job(
                my_job_second,
                next_run_time=jobs.filter(triger='second')[0].date_create,
                trigger=CronTrigger(second=f"*/{jobs.filter(triger='second')[0].period}"),
                id="my_job_second",  # The `id` assigned to each job MUST be unique
                max_instances=11,
                replace_existing=True,
            )
        except Exception as e:
            print(e)

        logger.info("Added job 'my_job'.")

        scheduler.add_job(
            delete_old_job_executions,
            trigger=CronTrigger(
                day_of_week="mon", hour="00", minute="00"
            ),  # Midnight on Monday, before start of the next work week.
            id="delete_old_job_executions",
            max_instances=1,
            replace_existing=True,
        )
        logger.info(
            "Added weekly job: 'delete_old_job_executions'."
        )

        try:
            logger.info("Starting scheduler...")
            scheduler.start()
        except KeyboardInterrupt:
            logger.info("Stopping scheduler...")
            scheduler.shutdown()
            logger.info("Scheduler shut down successfully!")


class Data(BaseCommand):
    help = "Runs APScheduler."

    def handle(self, jobs, *args, **options):
        global temp
        temp = jobs
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")
        try:
            scheduler.add_job(
                my_job_last,
                next_run_time=jobs.filter(triger='last')[0].date_create,
                trigger=CronTrigger(hour=f"*/{jobs.filter(triger='first')[0].period}"),
                id="my_job_last",  # The `id` assigned to each job MUST be unique
                max_instances=11,
                replace_existing=True,
            )
        except Exception as e:

            print(e)

        try:
            scheduler.add_job(
                my_job_first,
                next_run_time=jobs.filter(triger='second')[0].date_create,
                trigger=CronTrigger(hour=f"*/{jobs.filter(triger='first')[0].period}"),
                id="my_job_first",  # The `id` assigned to each job MUST be unique
                max_instances=11,
                replace_existing=True,
            )
        except Exception as e:
            print(e)

        logger.info("Added job 'my_job'.")

        scheduler.add_job(
            delete_old_job_executions,
            trigger=CronTrigger(
                day_of_week="mon", hour="00", minute="00"
            ),  # Midnight on Monday, before start of the next work week.
            id="delete_old_job_executions",
            max_instances=1,
            replace_existing=True,
        )
        logger.info(
            "Added weekly job: 'delete_old_job_executions'."
        )

        try:
            logger.info("Starting scheduler...")
            scheduler.start()
        except KeyboardInterrupt:
            logger.info("Stopping scheduler...")
            scheduler.shutdown()
            logger.info("Scheduler shut down successfully!")
