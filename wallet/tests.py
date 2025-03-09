from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

import uuid

from .models import Wallet

# тест для проверки баланса
class WalletDetailViewTest(TestCase):

    def test_get_wallet_detail(self):

        client = APIClient()  # Создаем клиент
        wallet = Wallet.objects.create(balance=100)  # Создаем кошелек
        url = reverse('wallet-detail', kwargs={'id': wallet.id})  # Получаем URL

        response = client.get(url)  # Отправляем GET запрос

        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Проверяем, что запрос успешен
        self.assertEqual(response.data['balance'], str(100))  # Проверяем баланс


#Тест для операций по счету
class WalletOperationViewTest(TestCase):

    def test_deposit(self):

        client = APIClient()
        wallet = Wallet.objects.create(balance=100)
        url = reverse('wallet-operation', kwargs={'id': wallet.id})
        data = {'operation_type': 'DEPOSIT', 'amount': 50}


        response = client.post(url, data, format='json')


        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['balance'], str(150))  # Проверяем, что баланс увеличился

    def test_withdraw(self):

        client = APIClient()
        wallet = Wallet.objects.create(balance=100)
        url = reverse('wallet-operation', kwargs={'id': wallet.id})
        data = {'operation_type': 'WITHDRAW', 'amount': 50}


        response = client.post(url, data, format='json')


        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['balance'], str(50))  # Проверяем, что баланс уменьшился