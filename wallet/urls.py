from django.urls import path

from . import views

urlpatterns = [
    path('wallets/<uuid:id>/', views.WalletDetailView.as_view(), name='wallet-detail'),
    path('wallets/<uuid:id>/operation', views.WalletOperationView.as_view(), name='wallet-operation'),
]