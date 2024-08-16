from rest_framework import serializers

from authentification.serializers import usergetSerializer
from .models import MovieComment
from authentification.models import User

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieComment
        fields = '__all__'

class CommentGetSerializer(serializers.ModelSerializer):
    user = usergetSerializer()
    class Meta:
        model = MovieComment
        fields = '__all__'