from django.db.models import Count
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from .models import Product, Collection
from .serializers import ProductSerializer, CollectionSerializer


# Create your views here.


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_serializer_context(self):
        return {"request": self.request}

    def destroy(self, request, *args, **kwargs):
        product = get_object_or_404(Product, pk=pk)
        if OrderItem.objects.filter(product=product).exists():
            return Response(
                {"error": "Product cannot be deleted as it has related order items"},
                status=status.HTTP_405_METHOD_NOT_ALLOWED,
            )
        return super().destroy(request, *args, **kwargs)


class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.annotate(products_count=Count("product")).all()
    serializer_class = CollectionSerializer

    def destroy(self, request, *args, **kwargs):
        collection = get_object_or_404(Collection, pk=pk)
        if Product.objects.filter(collection=collection).exists():
            return Response(
                {
                    "error": "Collection cannot be deleted as it has related order products"
                },
                status=status.HTTP_405_METHOD_NOT_ALLOWED,
            )
        return super().destroy(request, *args, **kwargs)
