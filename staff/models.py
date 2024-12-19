from django.db import models

# from accounts.models import Account
# from django.forms import *


class film(models.Model):
    movie_name = models.CharField(verbose_name="Nome do Filme", max_length=100)
    movie_genre = models.CharField(
        verbose_name="Gênero", max_length=100, null=True, blank=True
    )
    movie_lang = models.CharField(
        verbose_name="Idioma", blank=True, null=True, max_length=100
    )
    movie_year = models.IntegerField(verbose_name="Ano", blank=True, null=True)
    movie_plot = models.TextField(
        verbose_name="Sinopse", blank=True, null=True, help_text="Sinopse do Filme aqui"
    )
    url = models.URLField(blank=True, null=True)
    #     active = models.BooleanField(default=True)
    date_added = models.DateField(
        auto_now=False, auto_now_add=True, blank=True, null=True
    )

    def __str__(self):
        return self.movie_name


class banner(models.Model):
    movie = models.ForeignKey(
        film, verbose_name="Movie", on_delete=models.CASCADE, blank=True, null=True
    )
    url = models.URLField(verbose_name="Banner Image URL", blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.movie.movie_name


class show(models.Model):
    movie = models.ForeignKey(
        film, verbose_name="Movie", on_delete=models.CASCADE, blank=True, null=True
    )
    start_date = models.DateField(verbose_name="Data de Início", null=True)
    end_date = models.DateField(verbose_name="Data de Fim", null=True)
    price = models.PositiveIntegerField(verbose_name="Preço do Ingresso")
    showtime = models.TimeField(
        verbose_name="Horário",
        auto_now=False,
        auto_now_add=False,
        blank=True,
        null=True,
    )
    # modifiedby = models.OneToOneField(Account,on_delete=models.SET_NULL)

    def __str__(self):
        return self.movie.movie_name + "@" + self.showtime.strftime("%I:%M %p")
