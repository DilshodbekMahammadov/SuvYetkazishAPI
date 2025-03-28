"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from main.views import *

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework_simplejwt.views import token_obtain_pair, token_refresh

schema_view = get_schema_view(
   openapi.Info(
      title="Suv Yetkazish API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('suv/', SuvAPIView.as_view()),
    path('suv/<int:pk>/', SuvRetriveUpdateDeleteAPIView.as_view()),
    path('mijoz/', MijozAPIView.as_view()),
    path('mijoz/<int:pk>/', MijozRetriveUpdateDeleteAPIView.as_view()),
    path('buyrtma/', BuyurtmaListCreateAPIView.as_view()),
    path('administrator/', AdministratorListAPIView.as_view()),
    path('administrator/<int:pk>/', AdministratorRetriveAPIView.as_view()),
    path('haydovchi/', HaydovchiListAPIView.as_view()),
    path('haydovchi/<int:pk>/', HaydovchiRetriveAPIView.as_view())
]

urlpatterns += [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns += [
    path('api/token/', token_obtain_pair, name='token_obtain_pair'),
    path('api/token/refresh/', token_refresh, name='token_refresh'),
]