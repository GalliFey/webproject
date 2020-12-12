from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from django.db.models import Q

from .models import Anime, Genre


class GenreYear(object):
	def get_genres(self):
		return Genre.objects.all()

	def get_years(self):
		return Anime.objects.filter().values('year')
		



class AnimesView(GenreYear, ListView):
    model = Anime
    quaryset = Anime.objects.all()
    template_name = 'animes/animes.html'


class AnimeDetailView(GenreYear, DetailView):
    model = Anime
    slug_field = "url"


class FilterAnimesView(GenreYear, ListView):
    def get_queryset(self):
        queryset = Anime.objects.filter(
            Q(year__in=self.request.GET.getlist("year")) |
            Q(genres__in=self.request.GET.getlist("genre"))
        )
        return queryset


class Search(ListView):

    def get_queryset(self):
        return Anime.objects.filter(title__icontains=self.request.GET.get("q"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = f'q={self.request.GET.get("q")}&'
        return context