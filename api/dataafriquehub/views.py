from rest_framework.views import APIView
from rest_framework.response import Response
import requests
import os
from rest_framework import status
import tensorflow as tf
from rest_framework.permissions import AllowAny,IsAuthenticated
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import tokenizer_from_json
import re
import nltk
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import pickle

from rest_framework import viewsets
from .models import MovieComment
from .serializers import CommentSerializer,CommentGetSerializer
from django_filters.rest_framework import DjangoFilterBackend

class CommentViewSet(viewsets.ModelViewSet):
    queryset = MovieComment.objects.all()
    serializer_class = CommentGetSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['film_id']
    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        
        # Analyse de sentiment du commentaire
        new_review = request.data.get('content')
        # Prétraitement de la revue 
        new_review=preprocess_text(new_review)
        # Encodage de la revue
        encoded_review = tokenizer.texts_to_sequences([new_review])

        # Ajustement de la longueur de la séquence
        encoded_review = pad_sequences(encoded_review, maxlen=100)
        # Passage de la revue au modèle
        prediction = model.predict(encoded_review)
        sentiment_score = prediction[0][0]
        
        # Définir la valeur de 'review' en fonction du score de sentiment
        data['review'] = sentiment_score > 0.5
        
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)

        
        
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CommentGetSerializer
        return CommentSerializer
    def get_permissions(self):
            # Définir les autorisations en fonction de la méthode
            if self.action == 'list' or self.action == 'retrieve':
                permission_classes = [AllowAny]
            else:
                permission_classes = [AllowAny]
            return [permission() for permission in permission_classes]

def preprocess_text(text):
    # Suppression des balises HTML
    text = re.sub(r'<.*?>', '', text)
    
    # Suppression des stopwords
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text)
    filtered_text = [word for word in tokens if word.lower() not in stop_words]
    text = ' '.join(filtered_text)
    
    # Suppression de la ponctuation
    text = re.sub(r'[^\w\s]', '', text)
    # Suppression des lettres isolées
    text = re.sub(r'\b\w\b', '', text)
    return text
    
model = keras.models.load_model('../api/review_model/review_model.h5')
with open('../api/review_model/tokenizer.pkl', 'rb') as f:
    tokenizer= pickle.load(f)

from rest_framework.permissions import BasePermission

class AllowAnyOrAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user and request.user.is_authenticated or
            request.method in ['POST', 'GET']
        )
class PredictionReviewAPIView(APIView):
    permission_classes = [AllowAnyOrAuthenticated]
    def post(self, request):
        new_review = request.data.get('new_review')
        
        
        # Prétraitement de la revue 
        new_review=preprocess_text(new_review)
        # Encodage de la revue
        encoded_review = tokenizer.texts_to_sequences([new_review])

        # Ajustement de la longueur de la séquence
        encoded_review = pad_sequences(encoded_review, maxlen=100)
        # Passage de la revue au modèle
        prediction = model.predict(encoded_review)
        print(prediction)

        # Formatage de la réponse
        response = {
            'prediction': prediction.tolist()
        }
        
        return Response(response)



class MovieListView(APIView):
    permission_classes = [AllowAnyOrAuthenticated]
    def get(self, request, *args, **kwargs):
        url = "https://api.themoviedb.org/3/movie/top_rated?language=en-US&page=1"
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {os.environ.get('TMDBTOKEN')}" 
        }

        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            return Response(response.json(), status=status.HTTP_200_OK)
        else:
            return Response({"error": "Failed to fetch data from TheMovieDB"})

class MovieDetailView(APIView):
    permission_classes = [AllowAnyOrAuthenticated]
    def get(self, request, movie_id, *args, **kwargs):
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {os.environ.get('TMDBTOKEN')}"  
        }

        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            return Response(response.json(), status=status.HTTP_200_OK)
        else:
            return Response({"error": f"Failed to fetch data for movie ID {movie_id}"}, status=response.status_code)
