from django.urls import path
from mpesaApp.views import PayrollListView

urlpatterns = [
    path('', PayrollListView.as_view()),
]
