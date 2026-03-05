from django.shortcuts import render
from rest_framework.generics import (
    ListAPIView, CreateAPIView, RetrieveAPIView, 
    UpdateAPIView, DestroyAPIView   
)

from app.product.serializers import (
    CategorySerializers, TypesSerilaizers,
    ProductSerializer, ProductCreateSerializers
)
from app.product.models import Category, Types, Product

class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

class CategoryCreateAPIView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

class CategoryRetrieveAPIView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

class CategoryUpdateAPIView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

class CategoryDeleteAPIView(DestroyAPIView):
    queryset = Category.objects.all()

class TypesListAPIView(ListAPIView):
    queryset = Types.objects.all()
    serializer_class = TypesSerilaizers

class TypesCreateAPIView(CreateAPIView):
    queryset = Types.objects.all()
    serializer_class = TypesSerilaizers

class TypesRetrieveAPIView(RetrieveAPIView):
    queryset = Types.objects.all()
    serializer_class = TypesSerilaizers

class TypesUpdateAPIView(UpdateAPIView):
    queryset = Types.objects.all()
    serializer_class = TypesSerilaizers

class TypesDeleteAPIView(DestroyAPIView):
    queryset = Types.objects.all()

class ProductAPIView(ListAPIView):
    queryset = Product.objects.all().prefetch_related("images")
    serializer_class = ProductSerializer

    def get_serializer_context(self):
        ctx = super().get_serializer_context()
        ctx["request"] = self.request
        return ctx

class ProductCreateAPIView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializers

class ProductRetrieveAPIView(RetrieveAPIView):
    queryset = Product.objects.all().prefetch_related("images")
    serializer_class = ProductSerializer

    lookup_field = "uuid"
    lookup_url_kwarg = "uuid"

    def get_serializer_context(self):
        ctx = super().get_serializer_context()
        ctx["request"] = self.request
        return ctx

class ProductUpdateAPIView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializers

    lookup_field = "uuid"
    lookup_url_kwarg = "uuid"

class ProductDeleteAPIView(DestroyAPIView):
    queryset = Product.objects.all()

    lookup_field = "uuid"
    lookup_url_kwarg = "uuid"