# Generated by Django 4.1.3 on 2022-12-05 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0005_remove_banner_date_added_banner_modified'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='movie_plot',
            field=models.TextField(blank=True, null=True),
        ),
    ]
