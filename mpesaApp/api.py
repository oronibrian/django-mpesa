
from rest_framework import serializers
from mpesaApp.models import mpesaDetail,payment
from rest_framework.validators import UniqueTogetherValidator



class DetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = mpesaDetail
        fields = ('BusinessShortCode', 'Password', 'Timestamp','TransactionType',
        'PartyA','PartyB','CallBackURL','AccountReference','TransactionDesc')

        # read_only_fields = ('BusinessShortCode', 'Password', 'Timestamp','TransactionType',
        # 'PartyA','PartyB','CallBackURL','AccountReference','TransactionDesc')


class PaymentSerializer(serializers.ModelSerializer):
    """ A class to serialize payment as json compatible data """

    class Meta:
        model = payment

        fields = ('title', 'amount','phone','CheckoutRequestID',)
        read_only_fields=['CheckoutRequestID']

        
