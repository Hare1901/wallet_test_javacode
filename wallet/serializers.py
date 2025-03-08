
from rest_framework import serializers


from models import Wallet, Operations

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
	сериализатор для операций
	"""
	class Meta:
		model = Operations
		fields = ['operation_type', 'amount', 'created_at']