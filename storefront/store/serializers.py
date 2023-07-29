from decimal import Decimal
from rest_framework import serializers
from .models import Product, Collection


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ["id", "name", "featured_product", "created_by", "last_updated_by", "products_count"]

    products_count = serializers.IntegerField(read_only=True)
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "title", "slug", "description", "inventory", "price", "price_with_tax", "collection", "created_by", "last_updated_by"]

    price_with_tax = serializers.SerializerMethodField(method_name="calculate_tax")

    def calculate_tax(self, product: Product):
        return product.price * Decimal(1.1)
