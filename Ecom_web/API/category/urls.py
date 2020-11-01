from rest_framework import routers
from django.urls import path,include
from . import views
from datetime import datetime


router = routers.DefaultRouter()
router.register(r'', views.CategoryViewSet)


urlpatterns = [
    path('', include(router.urls)),
]