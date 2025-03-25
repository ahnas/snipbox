from rest_framework import serializers
from .models import Snippet, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'title']

class SnippetSerializer(serializers.ModelSerializer):
    tags = serializers.CharField(write_only=True, required=False)  # Accept as a string
    tag_names = serializers.SerializerMethodField()
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Snippet
        fields = ['id', 'title', 'note', 'created_at', 'updated_at', 'user', 'tags', 'tag_names']

    def create(self, validated_data):
        tags_str = validated_data.pop('tags', '')  # Get tags as a string (default empty)
        tags_list = [tag.strip() for tag in tags_str.split(",") if tag.strip()]  # Convert to list

        snippet = Snippet.objects.create(**validated_data)

        for tag_title in tags_list:
            tag, created = Tag.objects.get_or_create(title=tag_title)
            snippet.tags.add(tag)

        return snippet

    def get_tag_names(self, obj):
        return [tag.title for tag in obj.tags.all()] 

