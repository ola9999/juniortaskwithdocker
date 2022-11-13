from rest_framework import serializers
# from rest_framework.reverse import reverse
from django.urls import reverse
from juniortask.models import Author, Note

class AuthorSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Author
        fields = [
            'full_name',
            'date_birth',
            ]

    def get_full_name(self, obj):
        return f"{obj.first_name}  {obj.last_name}"


class NoteDetailsSerializer(serializers.ModelSerializer):
    author_details = AuthorSerializer(source='author',read_only=True)
    url = serializers.SerializerMethodField()

    class Meta:
        model = Note
        fields = [
            'pk',
            'author_details',
            'author',
            'content',
            'url',
        ]
        
    def get_url(self, obj):
        request = self. context.get('request') # self. request
        if request is None:
            return None
        return reverse ("note_detail", kwargs={"pk": obj.pk})
    
    def create(self, validated_data):
        obj = super().create(validated_data)
        return obj


