from django.urls import path
from .views import home, about, contact

urlpatterns = [
    path('', home.as_view(), name = 'home'),
    path('about/', about.as_view(), name = 'about'),
    path('contact/', contact.as_view(), name = 'contact')
]