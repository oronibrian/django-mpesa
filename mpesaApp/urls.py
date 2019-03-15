from django.urls import path
from mpesaApp.views import payment

urlpatterns = [
    path('', payment,name='payment'),
]
