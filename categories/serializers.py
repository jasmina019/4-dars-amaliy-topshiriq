from rest_framework import serializers
# from categories.models import Category


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    slug = serializers.SlugField()
    description = serializers.CharField()
    posts_count = serializers.SerializerMethodField()

    def get_posts_count(self, obj):
        return obj.posts.count()


# class CategorySerializer(serializers.ModelSerializer):
#     posts_count = serializers.SerializerMethodField()
#
#     class Meta:
#         model = Category
#         fields = ('id', 'name', 'slug', 'description', 'posts_count')
#
#     def get_posts_count(self, instance):
#         return instance.posts.count()
#
