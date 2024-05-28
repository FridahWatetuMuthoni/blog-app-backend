from rest_framework import serializers
from blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source="author.username", read_only=True)
    
    class Meta:
        model = Post
        fields = ['id','title','author_username', 'excerpt','published','content','category', 'image']
        read_only_fields = ['author_username', 'published', 'id']