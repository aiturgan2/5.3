from django.urls import path
from app.product.views import (
    CategoryListAPIView, CategoryCreateAPIView, CategoryRetrieveAPIView,
    CategoryUpdateAPIView, CategoryDeleteAPIView,
    TypesListAPIView, TypesCreateAPIView, TypesRetrieveAPIView,
    TypesUpdateAPIView, TypesDeleteAPIView,
    ProductAPIView, ProductCreateAPIView, ProductRetrieveAPIView, 
    ProductUpdateAPIView, ProductDeleteAPIView
)

urlpatterns = [
    path("category/", CategoryListAPIView.as_view(), name='category-list'),
    path("category/create/", CategoryCreateAPIView.as_view(), name='category-create'),
    path("category/<int:pk>/", CategoryRetrieveAPIView.as_view(), name='category-detail'),
    path("category/<int:pk>/update/", CategoryUpdateAPIView.as_view(), name='category-update'),
    path("category/<int:pk>/delete/", CategoryDeleteAPIView.as_view(), name='category-delete'),
    path("types/", TypesListAPIView.as_view(), name='types-list'),
    path("types/create/", TypesCreateAPIView.as_view(), name='types-create'),
    path("types/<int:pk>/", TypesRetrieveAPIView.as_view(), name='types-detail'),
    path("types/<int:pk>/update/", TypesUpdateAPIView.as_view(), name='types-update'),
    path("types/<int:pk>/delete/", TypesDeleteAPIView.as_view(), name='types-delete'),
    path("product/", ProductAPIView.as_view(), name='product-list'),
    path("product/create/", ProductCreateAPIView.as_view(), name='product-create'),
    path("product/<uuid:uuid>/", ProductRetrieveAPIView.as_view(), name='product-detail'),
    path("product/<uuid:uuid>/update/", ProductUpdateAPIView.as_view(), name='product-update'),
    path("product/<uuid:uuid>/delete/", ProductDeleteAPIView.as_view(), name='product-delete'),
]
