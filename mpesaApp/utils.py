import requests
from requests.auth import HTTPBasicAuth
from mpesaApp.models import  mpesaDetail,payment
from celery.utils.log import get_task_logger
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

def confirm_payment():

	payment = payment.objects.filter(payment_status_message="")

	for obj in payment:

		obj.success = False
		obj.payment_status_message="message"
		obj.save()

		logger.info( f'message {obj.payment_status_message}')

	return f"{obj.success}"


	# details = mpesaDetail.objects.all()

	# for val in details:
	# 	consumer_key = val.consumer_key

	# 	consumer_secret = val.CONSUMER_SECRET

	# 	token_api_URL = val.GENERATE_TOKEN_URL

	# 	r = requests.get(token_api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))

	# 	access_token = r.json()['access_token']

	# 	print('access_token-->>>>> {0}'.format(access_token))

	# 	api_url = str(val.api_url)
	# 	headers = {"Authorization": "Bearer %s" % access_token}


	# 	print(val)

	# payment = payment.objects.filter(payment_status_message="")

	# for obj in payment:

	# 	api_url = api_url_query


	# 	headers = {"Authorization": "Bearer %s" % access_token}
	# 	request = { "BusinessShortCode": val.BusinessShortCode ,
	# 	      "Password": val.Password,
	# 	      "Timestamp": val.Timestamp,
	# 	      "CheckoutRequestID": obj.CheckoutRequestID
	# 	}

	# 	response = requests.post(api_url, json = request, headers=headers)
	# 	code = response.json()['ResultCode']
	# 	message = response.json()['ResultDesc']
	# 	if code=="0":
	# 	    obj.success = True
	# 	    obj.payment_status_message=message

	# 	    obj.save()
	# 	else:
	# 	    obj.success = False
	# 	    obj.payment_status_message=message
	# 	    obj.save()


	# 	print (response.text)
	# return Response({'message': 'Payment Confirmed Successfully'}, status=status.HTTP_200_OK)