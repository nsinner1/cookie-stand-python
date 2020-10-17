from django.urls import path, include
from .views import SalesList, SalesDetail
from django.contrib import admin

urlpatterns = [
    path('', SalesList.as_view(), name='sales_list'),
    path('<int:pk>', SalesDetail.as_view(), name='sales_detail'),
    path('api-auth/', include('rest_framework.urls'))
]