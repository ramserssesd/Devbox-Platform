from django.urls import path
from .views import LoginView, ProfileView, APIUsageView

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('profile/', ProfileView.as_view()),
    path('api-usage/', APIUsageView.as_view()),
]
