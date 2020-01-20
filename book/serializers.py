from rest_framework import serializers

from book.models import Book


class BookSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Book
        fields = ["id", "name", "author"]


class BookCustomListSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Book
        fields = ["id", "name"]


class BookCustomDetailSerializer(serializers.ModelSerializer):

    is_premium = serializers.BooleanField(default=False)
    
    class Meta: 
        model = Book
        fields = ["id", "name", "is_premium"]