from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('display/', views.display, name='display'),
    path('add/', views.add_song, name='add_song'),
]
