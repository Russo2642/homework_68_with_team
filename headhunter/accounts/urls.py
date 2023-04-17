from accounts.views import (
    LoginView,
    RegisterView,
    logout_view,
    ProfileView,
    user_change_view
)
from django.urls import path


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('profile/<int:pk>/change', user_change_view, name='change'),
]
