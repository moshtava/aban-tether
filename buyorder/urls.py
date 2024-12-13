from django.urls import path
from .views import BuyOrderView

urlpatterns = [
    path('api/buy-order/', BuyOrderView.as_view(), name='buy-order'), 
]