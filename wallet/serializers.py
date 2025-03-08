
from rest_framework import serializers


from models import Wallet

class WalletSerializer(serializers.ModelSerializer):
	"""
	сериализатор для кошелька
	"""

	class Meta:
		model = Wallet
		fields = [
		    'id', 'balance'
		]


class OperationsSerializer(serializers.ModelSerializer):
	"""
	сериализатор для операций и amount
	"""
	operation_type = serializers.ChoiceField(choices=['DEPOSIT', 'WITHDRAW'])
	amount = serializers.DecimalField(max_digits=15, decimal_places=2)

	def validate_amount(self, value):
		"""
		проверка суммы ввода
		:param value: amount
		:return: amount>0
		"""
		if value <= 0:
			raise serializers.ValidationError("Сумма должна быть положительной.")
		return value