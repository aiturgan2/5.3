from django.urls import path
from app.product.views import (
    CategoryAPIView, TypesAPIView, ProductAPI
)

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("product", ProductAPI, basename='products')

urlpatterns = [
    path("category-list", CategoryAPIView.as_view(), name='category-list'),
    path("type-list", TypesAPIView.as_view(), name='type-list'),
    # path("product-list", ProductAPIView.as_view(), name='product-list'),

    # path("product-create", ProductCreateAPIView.as_view(), name='create'),
    # path("product-detail/<uuid:uuid>/", ProductRetrieveAPIView.as_view(), name='detail'),
    # path("product-update/<uuid:uuid>/update", ProductUpdateAPIView.as_view(), name='update'),
    # path("product-delete/<uuid:uuid>/delete", ProductDeleteAPIView.as_view(), name='delete'),
]

urlpatterns += router.urls
