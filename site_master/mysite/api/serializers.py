from rest_framework import serializers

from post.models import Post



class PostSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = "__all__"

# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(max_length=255)
#     author = serializers.CharField(max_length=50)
#     slug = serializers.SlugField(read_only=True)
#     content = serializers.CharField()
#     time_create = serializers.DateTimeField(read_only=True)
#     time_update = serializers.DateTimeField(read_only=True)
#     is_published = serializers.BooleanField(default=True)
#     cat_id = serializers.IntegerField()

#     def create(self, validate_data):
#         return Post.objects.create(**validate_data)

#     def update(self, instance, validate_data):
#         instance.title = validate_data.get("title", instance.title)
#         instance.author = validate_data.get("author", instance.author)
#         instance.slug = validate_data.get("slug", instance.slug)
#         instance.content = validate_data.get("content", instance.content)
#         instance.time_update = validate_data.get("time_update", instance.time_update)
#         instance.is_published = validate_data.get("is_published", instance.is_published)
#         instance.cat_id = validate_data.get("cat_id", instance.cat_id)
#         instance.save()
#         return instance
