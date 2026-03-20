from django.shortcuts import render
from rest_framework.generics import (
    ListAPIView, CreateAPIView, RetrieveAPIView, 
    UpdateAPIView, DestroyAPIView   
)

from rest_framework import mixins, filters
from rest_framework.viewsets import GenericViewSet
from django_filters.rest_framework import DjangoFilterBackend

from app.product.serializers import (
    CategorySerializers, TypesSerilaizers,
    ProductSerializer, ProductCreateSerializers
)
from app.product.models import Category, Types, Product
from app.paginatios import Pagination
from app.filters import ProductFilter

class CategoryAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers

class TypesAPIView(ListAPIView):
    queryset = Types.objects.all()
    serializer_class = TypesSerilaizers

class ProductAPI(mixins.ListModelMixin, 
                mixins.CreateModelMixin,
                mixins.UpdateModelMixin,
                mixins.RetrieveModelMixin,
                mixins.DestroyModelMixin,
                GenericViewSet):
    queryset = Product.objects.all()
    pagination_class = Pagination
    filter_backends = [
        DjangoFilterBackend, 
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    filterset_class = ProductFilter
    search_fields = ['title', 'description']
    ordering_fields = ['id', 'price', 'created_at']
    
    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return ProductSerializer
        if self.action in ["create", "update", "partial_update"]:
            return ProductCreateSerializers
        return ProductSerializer

    

# class ProductAPIView(ListAPIView):
#     queryset = Product.objects.all().prefetch_related("images")
#     serializer_class = ProductSerializer
# 
#     def get_serializer_context(self):
#         ctx = super().get_serializer_context()
#         ctx["reuqest"] = self.request
#         return ctx
# 
# class ProductCreateAPIView(CreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductCreateSerializers
# 
# class ProductRetrieveAPIView(RetrieveAPIView):
#     queryset = Product.objects.all().prefetch_related("images")
#     serializer_class = ProductSerializer
# 
#     lookup_field = "uuid"
#     lookup_url_kwarg = "uuid"
# 
#     def get_serializer_context(self):
#         ctx = super().get_serializer_context()
#         ctx["reuqest"] = self.request
#         return ctx
# 
# class ProductUpdateAPIView(UpdateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductCreateSerializers
# 
#     lookup_field = "uuid"
#     lookup_url_kwarg = "uuid"
# 
# class ProductDeleteAPIView(DestroyAPIView):
#     queryset = Product.objects.all()
# 
#     lookup_field = "uuid"
#     lookup_url_kwarg = "uuid"
