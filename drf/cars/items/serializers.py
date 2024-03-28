from rest_framework import serializers, viewsets, permissions, filters

# from django_filters.rest_framework import DjangoFilterBackend

from .models import Products, Images, Categories, Todo


# Serializers define the API representation.


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = "__all__"


class ItemsSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Products
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    items = ItemsSerializer(many=True, read_only=True)

    class Meta:
        model = Categories
        fields = "__all__"





class TodoSerializer(serializers.ModelSerializer):
    created = serializers.ReadOnlyField()
    completed = serializers.ReadOnlyField()

    class Meta:
        model = Todo
        fields = ["id", "title", "memo", "created", "completed"]


class TodoToggleCompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["id"]
        read_only_fields = ["title", "memo", "created", "completed"]
