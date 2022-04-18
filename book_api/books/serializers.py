from books.models import Author, Book, Category
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = (
            "uuid", "name", "description", "page", "author", "category"
        )
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["author"] = AuthorSerializer(instance.author).data
        representation["category"] = CategorySerializer(instance.category.all(), many=True).data
        return representation


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = (
            "uuid", "name", "created_at", "updated_at"
        )


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = (
            "uuid", "first_name", "last_name", "created_at", "updated_at"
        )
