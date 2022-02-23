from django.urls import path

from . import views

urlpatterns = [
    path('balance/',views.BalanceView),
    path('withdraw/',views.BalanceWithdrawView),
    path('deposit/',views.BalanceDepositView),
    path('customer/',views.AccountList.as_view()),
    path('customer/<int:pk>',views.AccountDetail.as_view()),
]