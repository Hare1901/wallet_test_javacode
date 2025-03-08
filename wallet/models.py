from django.db import models

import uuid

class Wallet(models.Model):
	"""
	класс для представления кошелька
	"""
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	balance = models.DecimalField(max_digits=15, decimal_places=2, default=0)


	def __str__(self):
		return f'Номер кошелька: {self.id}'


class Operations(models.Model):
	"""
	сохраняем операции
	"""
	OPERATIONS_TYPES = [
		('DEPOSIT', 'Deposit'),
		('WITHDRAW', 'Withdraw'),
	]

	wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='operations')
	operation_type = models.CharField(max_length=10, choices=OPERATIONS_TYPES, default='DEPOSIT')
	amount = models.DecimalField(max_digits=15, decimal_places=2)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f'{self.operation_type} of {self.amount} on {self.created_at}'
