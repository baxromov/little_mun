from django.urls import path, include
from users.views import registration

urlpatterns = [
    path('registration', registration, name='registration')
]
