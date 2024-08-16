from django.db import models

#prediction data model
from django.db import models
from authentification.models import User

class MovieComment(models.Model):
    user_name = models.CharField(max_length=100)
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    film_id = models.IntegerField()
    content = models.TextField()
    review = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Commentaire de {self.user_name} sur le film {self.film_id}"
