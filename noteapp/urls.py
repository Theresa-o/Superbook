from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('newnote', views.new_note, name='new_note'),
    path('update_note/<str:pk>', views.update_note, name="update_note"),
    path('delete_note/<str:pk>', views.delete_note, name="delete_note"),
    # path('search_note', views.search_note, name = 'search_note'),
]