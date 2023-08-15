from rest_framework import serializers

from ...models import Category, Product


# Serializers define the API representation.
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    products_count = serializers.SerializerMethodField(required=False)

    class Meta:
        model = Category
        fields = "__all__"

    def get_products_count(self, obj):
        return obj.products.count()
