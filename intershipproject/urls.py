"""intershipproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from django.conf.urls.static import static
from django.conf import settings
from product import views as productview
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', productview.product_list,name='product_list'),
    path('add_product/', productview.add_product,name="add_product"),
    path('edit_product/<int:id>', productview.edit_product,name="edit_product"),
    path('api/product',productview.ProductListCreate.as_view()),
    path('api/product/<int:pk>',productview.ProductupdateRetrieveDestroy.as_view())
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
