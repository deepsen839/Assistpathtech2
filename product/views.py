from django.shortcuts import render
from .forms import ProductForm
from .models import ProductModel
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import ProductSerializer
from rest_framework import filters
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
# Create your views here.
def add_product(request):

    productform = ProductForm(request.POST or None)
    if productform.is_valid():
        productform.save()
        return HttpResponse('<script type="text/javascript">window.opener.location.reload();window.close();</script>')
    else:
        return render(request,'product/add_product.html',{'productform':productform})

def product_list(request):
    all_products = ProductModel.objects.all()
    return render(request,'product/list_product.html',{'all_products':all_products})


def edit_product(request,id):
    product = ProductModel.objects.get(pk=id)
    productform = ProductForm(request.POST or None,instance=product)
    if productform.has_changed() and productform.is_valid():
        product.name = productform.cleaned_data['name']
        product.price = productform.cleaned_data['price']
        product.quantity = productform.cleaned_data['quantity']
        product.save()
        return HttpResponse('<script type="text/javascript">window.opener.location.reload();window.close();</script>')
    else:
        return render(request,'product/edit_product.html',{'productform':productform})

class ProductListCreate(ListCreateAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name',]

class ProductupdateRetrieveDestroy(RetrieveUpdateDestroyAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
       