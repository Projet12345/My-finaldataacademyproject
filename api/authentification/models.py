from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db import models

# modification du shéma de django par défaut pour inclure le role fournisseur et d'une méthode pour créer le fournisseur
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('L\'adresse email doit être spécifiée')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

    def create_adminuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_adminuser', True)
        return self.create_user(email, password, **extra_fields)
# définition d'un user personnalisé qui inclut le role de fournisseur
class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_supplier = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_admin(self):
        return self.is_superuser

    @property
    def is_employee(self):
        return self.is_staff

# pofile de l'utilisateur
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50,null=True)
    telmtn = models.CharField(max_length=50,null=True)
    telorange = models.CharField(max_length=50,null=True)
    description = models.TextField(null=True)
    adresse = models.TextField(null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

   