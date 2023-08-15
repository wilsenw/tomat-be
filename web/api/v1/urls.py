from django.urls import include, path
from rest_framework import routers

from . import viewsets

router = routers.DefaultRouter()
router.register("products", viewsets.ProductViewSet)
router.register("categories", viewsets.CategoryViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
