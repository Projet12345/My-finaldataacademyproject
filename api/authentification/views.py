from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordResetForm
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.conf import settings
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.permissions import AllowAny,IsAdminUser
from rest_framework.decorators import action
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics
from authentification.serializers import AdminUserSerializer,userSerializer,SuperUserSerializer, usergetSerializer
from authentification.serializers import UserProfilSerializer
from authentification.models import User, Profile
from django_filters.rest_framework import DjangoFilterBackend


from rest_framework.response import Response

"""
    Vue pour l'enregistrement d'un fournisseur avec email unique et un mot de passe.
"""
class AdminUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = AdminUserSerializer
    permission_classes = [IsAdminUser]
    http_method_names = ['post']


    #création d'un fournisseur
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
"""
    Vue pour l'enregistrement d'un client avec email unique et un mot de passe.
"""
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = userSerializer
    http_method_names = ['post']
    permission_classes = [AllowAny]

    #création d'un cient
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
"""
    Vue pour l'enregistrement d'un super user avec email unique et un mot de passe.
""" 
class SuperUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = SuperUserSerializer
    http_method_names = ['post']
    permission_classes = [IsAdminUser]

    # création d'un super user
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
"""
    Vue pour la connexion d'un utilisateur.
"""
class UserLoginView(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    http_method_names = ['post']
    queryset = User.objects.all()
    serializer_class = userSerializer
    

    def create(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(username=email, password=password)

        if user:
            login(request, user)
            refresh = RefreshToken.for_user(user)
            serializer = usergetSerializer(user)
            return Response({
                'status': 'success',
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': serializer.data
            })
        else:
            return Response({'status': 'fail'}, status=status.HTTP_400_BAD_REQUEST)

class UserLogoutView(viewsets.ModelViewSet):
    """
    Vue pour la déconnexion d'un utilisateur.
    """
    permission_classes = [AllowAny]
    http_method_names = ['post']
    queryset = User.objects.all()
    serializer_class = userSerializer

    def create(self, request):
        logout(request)
        return Response({'success': 'Vous êtes maintenant déconnecté.'}, status=status.HTTP_200_OK)


class PasswordResetView(viewsets.ModelViewSet):
    """
    Vue pour la réinitialisation de mot de passe.
    """
    permission_classes = [AllowAny]
    http_method_names = ['post']
    queryset = User.objects.all()
    serializer_class = userSerializer

    def create(self, request):
        form = PasswordResetForm(request.data)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                # Envoyer un email avec le lien de réinitialisation de mot de passe.
                send_mail(
                    'Réinitialisation de mot de passe',
                    'Cliquez sur ce lien pour réinitialiser votre mot de passe: http://localhost:8000/reset_password_confirm/',
                    settings.DEFAULT_FROM_EMAIL,
                    [email],
                    fail_silently=False,
                )
            except Exception as e:
                return Response({'error': 'Impossible d\'envoyer l\'email.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            return Response({'success': 'Un email avec un lien de réinitialisation de mot de passe a été envoyé.'}, status=status.HTTP_200_OK)
        else:
            errors = {}
            for field, error_list in form.errors.items():
                errors[field] = error_list[0]
            return Response({'error': errors}, status=status.HTTP_400_BAD_REQUEST)
"""
    Vue pour la gestion du user profile
"""
class UserViewprofil(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Profile.objects.all()
    serializer_class = UserProfilSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user']
    
