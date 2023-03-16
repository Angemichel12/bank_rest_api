from django.urls import path
from . import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register('categories', views.CategoryModelViewSet, basename='categories')
router.register('transactions', views.TransactionModelViewSet, basename='transactions')

urlpatterns = [
    path('currencies/', views.CurrencyListAPIView.as_view(), name='currencies'),
]+router.urls
