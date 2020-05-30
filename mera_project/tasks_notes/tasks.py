import datetime
import celery
from tasks_notes.models import UserInfo

@celery.decorators.periodic_task(run_every=datetime.timedelta(minutes=1))

def reset():
	uzer_qs = UserInfo.objects.all()
	for obj in range(len(uzer_qs)):
		uzer = uzer_qs[obj]
		total = uzer.total_exp
		total = 0
		uzer.total_exp = total
		uzer.save(update_fields=['total_exp'])
