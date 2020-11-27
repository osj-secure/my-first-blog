from django.urls import path
from playlist import views

app_name = 'playlist'
urlpatterns = [
    path('', views.PlaylistListView.as_view(),name='index'),
    path('add/', views.PlaylistCreateView.as_view(), name='add'),
    path('update/<int:pk>/', views.PlaylistUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.PlaylistDeleteView.as_view(), name='delete'),

    path('music/<int:pk>/', views.MusicDetailView.as_view(), name='music'),
    path('music/add/', views.MusicCreateView.as_view(), name='musicadd'),
    path('music/update/<int:pk>/', views.MusicUpdateView.as_view(), name='musicupdate'),
    path('music/delete/<int:pk>/', views.MusicDeleteView.as_view(), name='musicdelete'),
]