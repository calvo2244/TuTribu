
from django.urls import path, include
from Checkout.views import *

urlpatterns = [
    path('checkout/', include('Checkout.urls'))
]
