from rest_framework import serializers

from app.product.models import Category, Types, ProductImage, Product

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'image', 'crated_at']

class TypesSerilaizers(serializers.ModelSerializer):
    class Meta:
        model = Types
        fields = ['id', 'title', 'description', 'category', 'crated_at']

class ProductImageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = ProductImage
        fields = ['id', 'image', 'product']

    def get_image(self, obj):
        requets = self.context.get("request")
        url = obj.image.url
        return request.build_absolute_url(url) if request else url

class ProductSerializer(serializers.ModelSerializer):
    first_image = serializers.SerializerMethodField()
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = [
            'id', 'uuid', 'title', 'description',
            'category', 'types_product', 'created_at', 
            'price', 'first_image', 'images'
        ]

    def get_first_image(self, obj):
        fierts_img = obj.images.first()
        if fierts_img and fierts_img.image:
            request = self.context.get("request")
            url = fierts_img.image.url
            return request.build_absolute_uri(url) if request else url
        return None

class ProductCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "title", "description", "category",
            'types_product', 'price', 'is_active'
        ]

    def validate_price(self, value : str):
        try:
            num = float(value.replace(",", "."))
        except ValueError:
            raise serializers.ValidationError("price должен быть числом (1,99б 1.99)")

        if num <= 0:
            raise serializers.ValidationError("price должен быть больше 0")

        return value

    def validate(self, attrs):
        category = attrs.get("category") or getattr(self.instance, "category", None)
        types_product = attrs.get("types_product") or getattr(self.instance, "types_product", None)

        if category and types_product and types_product.category_id != category.id:
            raise serializers.ValidationError({
                "types_product" : "Этот тип не принадлежит выбранной категории!"  
            })

        return attrs