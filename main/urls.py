from django.urls import path
from .views import home, about, contact, user_profile


urlpatterns = [
    path('', home, name="home"),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('user/<int:user_id>/profile/', user_profile, name='userprofile'),
]

