import json
from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
# from django.core.exceptions import MultipleObjectsReturned
# from rest_framework import permissions

#Models and serializers
from .models import Account
from .serializers import AccountSerializer, AccountBalanceSerializer
#These two are used to tell the response type of our API in @extend_schema for /docs route.
from .serializers import AccountBalanceResponsetSerializer, AccountBalanceResponseSerializer

#Function Based View
from rest_framework.decorators import api_view
#For Docs Generation
from drf_spectacular.utils import extend_schema 



#Get all accounts and create new ones
class AccountList(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = AccountSerializer


# RetrieveUpdateDestroyAPIView -- This can be used instead of DestroyAPIView To allow Read,update,delete
#Delete accounts
class AccountDetail(generics.DestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer



@extend_schema(request=AccountBalanceResponseSerializer, responses=AccountBalanceSerializer)
@api_view(['POST'])
def BalanceView(request):

  if request.method == 'POST':
    ##Send this in post request: {"cardNumber": "4422", "pin": "4422"} #data sample
    data = request.data
    cardNumber = data["cardNumber"]

    # try:
    #     customer = Account.objects.get(cardNumber=cardNumber)
    #     serializer = AccountBalanceSerializer(customer)
    #     return Response(serializer.data)  
    # except MultipleObjectsReturned as e:
    #     return Response({'detail': 'Error occured'})

    customer = get_object_or_404(Account, cardNumber=cardNumber)
    serializer = AccountBalanceSerializer(customer)
    return Response(serializer.data)  
  else:
    return Response({'detail': 'method not allowed'})



@extend_schema(request=AccountBalanceResponsetSerializer, responses=AccountBalanceSerializer)
@api_view(['POST'])
def BalanceWithdrawView(request):

  if request.method == 'POST':
     #Send this in post request: {"cardNumber": "4422", "pin": "4422","amount": "100"}
    data = request.data
    cardNumber = data["cardNumber"]
    pin = data["pin"]
    amount = data["amount"]
    print(request.data)
    try:
        customer = Account.objects.get(cardNumber=cardNumber)
        if (customer.pin == pin) and (int(customer.balance) >= int(amount)):
          serializer = AccountBalanceSerializer(customer, many=False)
          customer.balance = int(customer.balance) - int(amount)          
          customer.save()
          return Response(serializer.data)
        else:
          return Response({'detail': 'Not Enough Funds'})
    except Exception as e:
        return Response({'detail': 'Error occured'})

  else:
    return Response({'detail': 'Error occured'})



@extend_schema(request=AccountBalanceResponsetSerializer, responses=AccountBalanceSerializer)
@api_view(['POST'])
def BalanceDepositView(request):

  if request.method == 'POST':
     #Send this in post request: {"cardNumber": "4422", "pin": "4422","amount": "270"}
    data = request.data
    cardNumber = data["cardNumber"]
    amount = data["amount"]
    pin = data["pin"]

    try:
        customer = Account.objects.get(cardNumber=cardNumber)
        if (customer.pin == pin) and amount:
          serializer = AccountBalanceSerializer(customer, many=False)
          customer.balance = int(customer.balance) + int(amount)          
          customer.save()
          return Response(serializer.data)
        else:
          return Response({'detail': 'Invalid credentials'})

        # trick to handle if statements. it works the same as above
        # if (customer.pin != pin) or not(amount):
        #   return Response({'detail': 'Invalid credentials'})

        # serializer = AccountBalanceSerializer(customer, many=False)
        # customer.balance = int(customer.balance) + int(amount)          
        # customer.save()
        # return Response(serializer.data)
          
    except Exception as e:
        return Response({'detail': 'Error occured'})

  else:
    return Response({'detail': 'Error occured'})