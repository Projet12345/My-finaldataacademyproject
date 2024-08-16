from rest_framework import routers

from .views import UserLoginView,AdminUserViewSet,UserViewSet,SuperUserViewSet,UserLogoutView,PasswordResetView
from .views import UserViewprofil
router = routers.DefaultRouter()
router.register('auth/login', UserLoginView, basename='user-login')
router.register('auth/logout', UserLogoutView, basename='user-logout')
router.register('auth/reset-password', PasswordResetView, basename='user-reset-password')
router.register('users/create-user', UserViewSet, basename='create-user')
router.register('users/create-admin', AdminUserViewSet, basename='create-admin-user')
router.register('users/create-superadmin', SuperUserViewSet, basename='create-super-user')
router.register('users/profile', UserViewprofil, basename='user-profile')