from rest_framework import generics, status
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from django.db import transaction

from .models import Wallet
from .serializers import WalletSerializer, OperationsSerializer


class WalletDetailView(generics.RetrieveAPIView):
    '''
    Счет кошелька
    '''
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    lookup_field = 'id'

class WalletOperationView(generics.GenericAPIView):
    """
    Выполнение запроса
    """
    serializer_class = OperationsSerializer

    def post(self, request, id):
        wallet = get_object_or_404(Wallet, id=id)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        operation_type = serializer.validated_data['operation_type']
        amount = serializer.validated_data['amount']

        with transaction.atomic():  # Обеспечиваем атомарность операции
            if operation_type == 'DEPOSIT':
                wallet.balance += amount
            elif operation_type == 'WITHDRAW':
                if wallet.balance < amount:
                    return Response({"error": "Недостаточно средств."}, status=status.HTTP_400_BAD_REQUEST)
                wallet.balance -= amount
            wallet.save()

        return Response(WalletSerializer(wallet).data, status=status.HTTP_200_OK)