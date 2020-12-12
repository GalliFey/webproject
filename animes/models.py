from django.db import models 


from django.urls import reverse



class Genre(models.Model):
    name = models.CharField("Имя", max_length=100)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class Anime(models.Model):

    title = models.CharField("Название", max_length=100)
    tagline = models.CharField("Слоган", max_length=100, default='')
    description = models.TextField("Описание")
    poster = models.ImageField("Постер", upload_to="posters/")
    year = models.PositiveSmallIntegerField("Дата выхода", default=2019)
    country = models.CharField("Страна", max_length=30)
    directors = models.CharField(verbose_name="режиссер", max_length=100)
    genres = models.ManyToManyField(Genre, verbose_name="жанры")  
    url = models.SlugField(max_length=130, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("anime_detail", kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Аниме"
        verbose_name_plural = "Аниме"


class Reviews(models.Model):
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    anime = models.ForeignKey(Anime, verbose_name="Аниме", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.movie}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"