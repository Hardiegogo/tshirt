from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from .models import Order
from .serializers import OrderSerializer
from django.http import JsonResponse

# Create your views here.

def validate_user_session_token(id, token):
    Usermodel=get_user_model()
    try:
        user=Usermodel.objects.get(pk=id)
        if user.session_token == token:
            return True
        return False
    except user.DoesNotExist:
        return False

@csrf_exempt
def add(request,id,token):
    if not validate_user_session_token(id,token):
        return JsonResponse({'error':'Please re-Login'})

    if request.method=='POST':
        user_id=id
        products=request.POST['producgts']
        amount=request.POST['amount']
        transaction_id=request.POST['transaction_id']
        total_products=len(products.split(','))

    Usermodel=get_user_model()
    try:
        user=Usermodel.objects.get(pk=id)

    except user.DoesNotExist:
        return JsonResponse({'error':'User does not exists'})

    ordr=Order(user=user,total_products=products,product_names=products,total_amount=amount,transaction_id=transaction_id)
    ordr.save()
    return JsonResponse({'success':True,'error':False,'msg':'Order placed successfully'})

class OrderViewSet(viewsets.ModelViewSet):
    queryset=Order.objects.all().order_by('id')
    serializer_class=OrderSerializer