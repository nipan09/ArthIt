from celery.decorators import periodic_task
from celery.task.schedules import crontab
from tasks_notes.models import BudgetInfo

@periodic_task(run_every=(crontab(minute='*/15')))
def monthly_starting_value():
	value=6
	return value
