from rest_framework import generics

from library.models import Category
from library.serializers import CategorySerializer


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()