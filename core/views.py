from .serializers import (CurrencyModelSerializer, 
                          CategoryModelSerializer,
                          WriteTransactionModelSerializer,
                          ReadTransactionModelSerializer)
from rest_framework import generics
from .models import (Currency,
                     Category,
                     Transaction)
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class CurrencyListAPIView(generics.ListAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencyModelSerializer

class CategoryModelViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer

class TransactionModelViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.select_related()
    filter_backends = (SearchFilter,OrderingFilter, DjangoFilterBackend)
    search_fields = ('description',)
    ordering_fields = ('amount', 'date')
    filterset_fields = ('currency__code',)
    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return ReadTransactionModelSerializer
        return WriteTransactionModelSerializer



