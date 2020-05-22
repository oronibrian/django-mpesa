from django.db import models

# Create your models here.


class mpesaDetail(models.Model):
    api_url = models.CharField(max_length=255)
    BusinessShortCode = models.CharField(max_length=255)
    Password = models.CharField(max_length=255)
    Timestamp = models.CharField(max_length=255)
    TransactionType = models.CharField(max_length=255)
    PartyA = models.CharField(max_length=255)
    PartyB = models.CharField(max_length=255)
    CallBackURL = models.CharField(max_length=255)
    AccountReference = models.CharField(max_length=255)
    TransactionDesc = models.CharField(max_length=255)

    consumer_key = models.CharField(max_length=255)
    CONSUMER_SECRET = models.CharField(max_length=255)
    GENERATE_TOKEN_URL = models.CharField(max_length=255)

    def __str__(self):
        return self.BusinessShortCode

class payment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    amount = models.IntegerField()
    phone=models.CharField(max_length=100)
   

    class Meta:
        ordering = ('created',)
    
    def __str__(self):
        return self.title