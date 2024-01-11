from django.urls import path
from .views import Home, UserCreate,BookListCreateView,BookRetrieveUpdateDestroyView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("home/",Home.as_view(), name='home'),
    path("book/",BookListCreateView.as_view(),name="list_create_view"),
    path("book/<int:pk>/",BookRetrieveUpdateDestroyView.as_view(),name="update_delete_view"),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]