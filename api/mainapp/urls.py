
from django.contrib import admin
from django.urls import path
from django.urls import path,include, re_path
from django.conf.urls.static import static
from rest_framework import routers
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

from dataafriquehub.views import PredictionReviewAPIView,MovieListView,MovieDetailView
from dataafriquehub.urls import router as dataafriquerouter
from authentification.urls import router as authentificationrouter
# swagger
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
schema_view = get_schema_view(
   openapi.Info(
      title="Data Afrique Hub API Project",
      default_version='v1',
      description="Movies Costumers Review by Nguetoum anderson",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="nguetoumanderson@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

#routes for app
router = routers.DefaultRouter() 
router.registry.extend(authentificationrouter.registry)
router.registry.extend(dataafriquerouter.registry)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
   #  auth UserLoginView
    path('api/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/token/access/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # Model
    path('api/predict-review/', PredictionReviewAPIView.as_view(), name='predictreview'),
    path('api/movies-list/', MovieListView.as_view(), name='movieslistview'),
    path('api/movies/<int:movie_id>/', MovieDetailView.as_view(), name='movie-detail'),
    #rest password
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]

urlpatterns += staticfiles_urlpatterns()
