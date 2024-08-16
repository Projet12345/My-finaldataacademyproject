from rest_framework import serializers
from authentification.models import User, Profile


"""
    serializer pour les utilisateurs clients
"""
class usergetSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email', 'password','is_superuser','is_supplier']
        extra_kwargs = {'password': {'write_only': True}}
class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

        def validate_email(self, value):
            """
            Vérifier si l'email existe déjà dans la base de données.
            """
            if User.objects.filter(email=value).exists():
                raise serializers.ValidationError("Cet email existe déjà.")
            return value

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
"""
    serializer pour les utilisateurs fournisseurs
"""
class AdminUserSerializer(userSerializer):
    class Meta:
        model = User
        fields = ['id','email', 'password']
        extra_kwargs = {'password': {'write_only': True}}
        def validate_email(self, value):
            """
            Vérifier si l'email existe déjà dans la base de données.
            """
            if User.objects.filter(email=value).exists():
                raise serializers.ValidationError("Cet email existe déjà.")
            return value
    def create(self, validated_data):
        user = User.objects.create_user_supplier(**validated_data)
        return user
"""
    serializer pour les super utilisateurs
"""
class SuperUserSerializer(userSerializer):
    class Meta:
        model = User
        fields = ['id','email', 'password']
        extra_kwargs = {'password': {'write_only': True}}
        def validate_email(self, value):
            """
            Vérifier si l'email existe déjà dans la base de données.
            """
            if User.objects.filter(email=value).exists():
                raise serializers.ValidationError("Cet email existe déjà.")
            return value
    def create(self, validated_data):
        user = User.objects.create_superuser(**validated_data)
        return user
"""
    serializer pour les profils des uers
"""
class UserProfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
