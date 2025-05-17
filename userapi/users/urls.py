from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    UserViewSet,
    login_view,
    register_view,
    logout_view,
    user_list,
    add_user,
    edit_user,
    delete_user
)

# Router setup for API endpoints
router = DefaultRouter()
router.register(r'api/users', UserViewSet)

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('user_list/', user_list, name='user_list'),
    path('add/', add_user, name='add_user'),
    path('edit/<int:user_id>/', edit_user, name='edit_user'),
    path('delete/<int:user_id>/', delete_user, name='delete_user'),
    path('', include(router.urls)),
]
