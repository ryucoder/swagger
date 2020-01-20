from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from book.serializers import BookSerializer, BookCustomListSerializer
from book.models import Book



class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    
    @action(detail=False, methods=['get'])
    def custom_list(self, request, pk=None):
        
        serializer = BookCustomListSerializer()
        print()
        print()
        print("Damn! I was printed!!")
        print()
        print()

        return Response(serializer.errors, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def custom_detail(self, request, pk=None):
        
        print()
        print()
        print("Damn! I was printed!!")
        print()
        print()

        return Response(serializer.errors, status=status.HTTP_200_OK)