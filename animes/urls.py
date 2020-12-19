from django.urls import path

from . import views


urlpatterns = [
	path('', views.AnimesView.as_view(), name='home'),
	path("filter/", views.FilterAnimesView.as_view(), name='filter'),
	path("search/", views.Search.as_view(), name='search'),
	path('<slug:slug>/', views.AnimeDetailView.as_view(),name='anime_detail'),

]