# Generated by Django 4.1.3 on 2024-11-21 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0010_alter_banner_movie_alter_banner_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='movie_genre',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Gênero'),
        ),
        migrations.AlterField(
            model_name='film',
            name='movie_lang',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Idioma'),
        ),
        migrations.AlterField(
            model_name='film',
            name='movie_name',
            field=models.CharField(max_length=100, verbose_name='Nome do Filme'),
        ),
        migrations.AlterField(
            model_name='film',
            name='movie_plot',
            field=models.TextField(blank=True, help_text='Sinopse do Filme aqui', null=True, verbose_name='Sinopse'),
        ),
        migrations.AlterField(
            model_name='film',
            name='movie_year',
            field=models.IntegerField(blank=True, null=True, verbose_name='Ano'),
        ),
    ]
