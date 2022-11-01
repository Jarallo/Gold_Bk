"""Gold_Bk URL Configuration

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
from django.urls import path, include
from rest_framework import routers
from Gold_Bk_app.views import *

router = routers.DefaultRouter()
router.register('activo', Activo_View, basename='activo')
router.register('trade', Trade_View, basename='trade')
router.register('cuenta', Cuenta_View, basename='cuenta')
router.register('usuario', Usuario_View, basename='usuario')



urlpatterns = [
    path('', include(router.urls)),
    path('token', CustomAuthToken.as_view(), name ='token'),
    path('admin/', admin.site.urls),
]