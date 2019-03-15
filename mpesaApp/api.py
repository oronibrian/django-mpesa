
from rest_framework import serializers
from mpesaApp.models import mpesaDetail

class DetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = mpesaDetail
        fields = ('BusinessShortCode', 'Password', 'Timestamp','TransactionType',
        'PartyA','PartyB','CallBackURL','AccountReference','TransactionDesc')

        # read_only_fields = ('BusinessShortCode', 'Password', 'Timestamp','TransactionType',
        # 'PartyA','PartyB','CallBackURL','AccountReference','TransactionDesc')
  