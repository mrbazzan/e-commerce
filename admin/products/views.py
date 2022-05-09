from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import ProductSerializer
from .models import Product, User
from .producer import publish

import random


class ProductViewSet(viewsets.ViewSet):
    def list(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        publish()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @staticmethod
    def get_product(pk=None):
        return get_object_or_404(Product, pk=pk)

    def retrieve(self, request, pk=None):
        product = self.get_product(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def _update(self, request, pk, partial=False):
        product = self.get_product(pk)
        serializer = ProductSerializer(instance=product, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def update(self, request, pk=None):
        return self._update(request, pk=pk)

    def partial_update(self, request, pk=None):
        return self._update(request, pk=pk, partial=True)

    def destroy(self, request, pk=None):
        product = self.get_product(pk)
        product.delete()
        return Response(
            {"delete": f"Product(id={pk}) successfully deleted."},
            status=status.HTTP_204_NO_CONTENT
        )


class UserAPIView(APIView):
    def get(self, _):
        try:
            user = random.choice(User.objects.all())
        except IndexError:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response({
            "id": user.id
        }, status=status.HTTP_200_OK)
