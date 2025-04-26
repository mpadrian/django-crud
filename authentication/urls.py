from django.urls import path,include
from .views import SignUpView
from authentication.views import SignUpView, CustomLoginView, HomeView
from django.contrib import admin

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('', HomeView.as_view(), name='home'),
]