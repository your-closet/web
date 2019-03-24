from django.urls import path
from . import views

urlpatterns = [
    path(
        '',
        views.index,
        name='index',
    ),
    path('signup/', views.signup, name='signup'),
    path('add_clothing/', views.add_clothing, name='add_clothing'),
    path('get_clothing/', views.get_clothing, name='get_clothing'),
    path('test/',views.test, name='test'),
]
