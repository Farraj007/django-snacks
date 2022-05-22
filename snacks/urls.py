from django.urls import path
from .views import HomeView, AboutView

urlpatterns = [
    path('', HomeView.as_view(), name='Home'),
    path('About', AboutView.as_view(), name='About'),
]