from django.urls import path, include
from users.views import registration, login_view, logout_view

urlpatterns = [
    path('registration', registration, name='registration'),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout')
]
