from django.urls import path
from . import views
from rest_framework import routers
from .views import BookViewSet

router = routers.DefaultRouter()
router.register('book', BookViewSet)

urlpatterns = [
    path('first', views.first),
]
