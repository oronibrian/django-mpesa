from django.shortcuts import render
from django.http import HttpResponse
from mpesaApp.models import mpesaDetail
from mpesaApp.api import DetailsSerializer
import json
from django.core import serializers
import requests
from requests.auth import HTTPBasicAuth
from django.http import JsonResponse
from rest_framework.renderers import JSONRenderer

import io
from rest_framework.parsers import JSONParser

import pprint
import ast


def payment(request):
    details = mpesaDetail.objects.all()


    print('*******  Reached here  *************')
    print(details)

    serializer = DetailsSerializer(details,many=True)

    parameter = json.dumps(serializer.data[0])

    numbber_amount = json.dumps({"Amount":10,"PhoneNumber":str("254702357053")})


    jsonMerged = {**json.loads(parameter), **json.loads(numbber_amount)}

    payload = json.dumps(jsonMerged,indent=4)

    print(payload)


    for val in details: 

        consumer_key = val.consumer_key

        consumer_secret = val.CONSUMER_SECRET

        token_api_URL = val.GENERATE_TOKEN_URL

        r = requests.get(token_api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))

        access_token=r.json()['access_token']



        print('access_token-->>>>> {0}'.format(access_token))

        api_url = str(val.api_url)
        headers = { "Authorization": "Bearer %s" % access_token } 
        # params={
             
        #          "BusinessShortCode": val.BusinessShortCode,
        #         "Password": val.Password,
        #         "Timestamp": val.Timestamp,
        #         "TransactionType": val.TransactionType,
        #         "PartyA": val.PartyA,
        #         "PartyB": str(val.PartyB),
        #         "CallBackURL": val.CallBackURL,
        #         "AccountReference": val.AccountReference,
        #         "TransactionDesc": val.TransactionDesc,
        #         "Amount": 10,
        #         "PhoneNumber": str("254702357053"),


        # }

        params=ast.literal_eval(payload)
        
        response = requests.post(api_url,json=params, headers=headers)

        pprint.pprint(response)


        print("Params:{0} ".format(params))

    
    return HttpResponse(response)
