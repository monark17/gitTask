# yourappname/urls.py
from django.urls import path
from .views import index, register, add_note, login_redirect, view_notes, user_profile

urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('add_note/', add_note, name='add_note'),
    path('login_redirect/', login_redirect, name='login_redirect'),
    path('profile/', user_profile, name='user_profile'),
    path('view_notes/', view_notes, name='view_notes'),
]