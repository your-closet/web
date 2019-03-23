from django.urls import path
from . import views

urlpatterns = [
    path(
        '',
        views.index,
        name='index',
    ),
    path(
        'clothing_add',
        views.CreateClothingItem.as_view(),
        name='clothing_add'),
    path(
        'clothing_edit',
        views.ClothingItemUpdate.as_view(),
        name='clothing_edit'),
    path(
        'clothing_delete',
        views.ClothingItemDelete.as_view(),
        name='clothing_delete'),
    path('signup/', views.signup, name='signup'),
]
