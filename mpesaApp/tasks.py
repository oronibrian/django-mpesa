from __future__ import absolute_import, unicode_literals
from celery import task
from celery.utils.log import get_task_logger

from mpesaApp.models import  mpesaDetail,payment

logger = get_task_logger(__name__)



@task()
def comrfirm_payment_task():

	objects = payment.objects.filter(payment_status_message="")

	for obj in objects:

		obj.success = False
		obj.payment_status_message="message"
		obj.save()

		logger.info( f'message {obj.payment_status_message}')


	return f"Obje{objects}"