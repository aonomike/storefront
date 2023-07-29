from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CollectionViewSet

router = DefaultRouter()
router.register("products", ProductViewSet)
router.register("collections", CollectionViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
