from rest_framework import serializers
from .models import Product,Image
from comment.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Comment
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    name = serializers.CharField() 
    image = serializers.ImageField() 

    class Meta:
        model  = Image
        fields = ['name', 'image']

class ProductSerializer(serializers.ModelSerializer):
    comment = serializers.SerializerMethodField()
    image = ImageSerializer(many=True)
    
    class Meta:
        model  = Product
        fields = ['id', 'name', 'price', 'image', 'description', 'slug', 'created_at', 'comment']

    def get_comment(self, obj):
        comment_details = Comment.objects.filter(product=obj)
        serializer = CommentSerializer(comment_details, many=True)
        return serializer.data