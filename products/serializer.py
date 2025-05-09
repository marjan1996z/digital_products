from rest_framework import serializers

from products.models import Category, Product, File

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title', 'description', 'avatar')

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('id', 'title', 'file', 'file_type')

class ProductSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)
    # files = FileSerializer(many=True)

    class Meta:
        model = Product
        fields = ('id','title', 'description', 'avatar', 'categories', 'url')