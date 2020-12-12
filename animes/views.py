from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import Anime


class AnimesView(ListView):
    model = Anime
    quaryset = Anime.objects.all()
    template_name = 'animes/animes.html'


class AnimeDetailView(DetailView):
    model = Anime
    slug_field = "url"
