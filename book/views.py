from pprint import pprint

from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.schemas.openapi import AutoSchema

from book.serializers import BookSerializer, BookCustomListSerializer, BookCustomDetailSerializer
from book.models import Book


class CustomSchema(AutoSchema):
    def get_operation(self, *args, **kwargs):
        # Implement custom introspection here (or in other sub-methods)

        operation = super(CustomSchema, self).get_operation(*args, **kwargs)

        # modify the operation he for fine grain control over what you want to show in docs

        return operation  
        

class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    schema = CustomSchema()


    @action(detail=False, methods=['get'], serializer_class=BookCustomListSerializer)
    def custom_list(self, request, pk=None):
        
        # serializer = BookCustomListSerializer()
        print()
        print()
        print("Damn! I was printed!!")
        print()
        print()

        return Response(serializer.errors, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'], serializer_class=BookCustomDetailSerializer)
    def custom_detail(self, request, pk=None):
        
        # instance = BookCustomDetailSerializer.objects.get()
        print()
        print()
        print("Damn! I was printed!!")
        print()
        print()

        return Response(serializer.errors, status=status.HTTP_200_OK)
    
    
    # Pass schema=None into the action decorator to disaable the documentation of a particular endpoint.
    # @action(detail=True, methods=['post'], schema=None)
    # def custom_detail(self, request, pk=None):
    #     return Response(serializer.errors, status=status.HTTP_200_OK)


