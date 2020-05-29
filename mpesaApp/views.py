import ast
import json
import pprint

import requests
from django.http import HttpResponse
from requests.auth import HTTPBasicAuth

from mpesaApp.api import DetailsSerializer
from mpesaApp.models import mpesaDetail
from .api import PaymentSerializer
from rest_framework import generics
from .models import payment
from rest_framework.response import Response
from rest_framework import status



class PayrollListView(generics.ListCreateAPIView):
    queryset = payment.objects.all()
    serializer_class = PaymentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        details = mpesaDetail.objects.all()
        serializer1 = self.get_serializer(data=request.data)

        serializer1.is_valid(raise_exception=True)
        serializer1.validated_data
        
        print(serializer1.is_valid())


        amount1 = serializer1.validated_data['amount']
        phone = serializer1.validated_data['phone']
        title = serializer1.validated_data['title']

        data = request.POST.dict()
        title = str(title)

        price = str(amount1)
        number = str("254" + phone[1:])

        print(amount1, phone)

        print('*******  Stk payload here  *************')
        print(details)

        serializer = DetailsSerializer(details, many=True)

        parameter = json.dumps(serializer.data[0])

        numbber_amount = json.dumps({"Amount": price, "PhoneNumber": number})

        jsonMerged = {**json.loads(parameter), **json.loads(numbber_amount)}

        payload = json.dumps(jsonMerged, indent=4)

        print(payload)

        for val in details:
            consumer_key = val.consumer_key

            consumer_secret = val.CONSUMER_SECRET

            token_api_URL = val.GENERATE_TOKEN_URL

            r = requests.get(token_api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))

            access_token = r.json()['access_token']

            print('access_token-->>>>> {0}'.format(access_token))

            api_url = str(val.api_url)
            headers = {"Authorization": "Bearer %s" % access_token}

            params = ast.literal_eval(payload)

            response = requests.post(api_url, json=params, headers=headers)

            CheckoutRequestID = response.json()['CheckoutRequestID']

            pprint.pprint(CheckoutRequestID)


            print("Params:{0} ".format(params))

        serializer1.validated_data['CheckoutRequestID']=CheckoutRequestID

        obj = payment.objects.get(title=title)
        if not obj:
            serializer1.save()
            api_url_query = "https://sandbox.safaricom.co.ke/mpesa/stkpushquery/v1/query"

            confirm_payment(title,api_url_query,access_token,val.BusinessShortCode,val.Timestamp,val.Password,CheckoutRequestID)
        else:

            obj.CheckoutRequestID = CheckoutRequestID
            obj.save()
            api_url_query = "https://sandbox.safaricom.co.ke/mpesa/stkpushquery/v1/query"

            confirm_payment(title,api_url_query,access_token,val.BusinessShortCode,val.Timestamp,val.Password,CheckoutRequestID)



        return Response({'message': 'Payment Processed Successfully'}, status=status.HTTP_200_OK)



def confirm_payment(title,api_url_query,access_token,BusinessShortCode,Timestamp,Password,CheckoutRequestID):

    api_url = api_url_query

    obj = payment.objects.get(title=title)


    headers = {"Authorization": "Bearer %s" % access_token}
    request = { "BusinessShortCode": BusinessShortCode ,
          "Password": Password,
          "Timestamp": Timestamp,
          "CheckoutRequestID": CheckoutRequestID
    }

    response = requests.post(api_url, json = request, headers=headers)
    # code = response.json()['ResultCode']
    # message = response.json()['ResultDesc']
    # if code=="0":
    #     obj.success = True
    #     obj.payment_status_message=message

    #     obj.save()
    # else:
    #     obj.success = False
    #     obj.payment_status_message=message
    #     obj.save()


    print (response.text)
    return Response({'message': 'Payment Confirmed Successfully'}, status=status.HTTP_200_OK)