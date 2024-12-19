# booking/tests.py
from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import Account
from booking.models import booking
from staff.models import film, show, banner
from datetime import datetime, timezone, timedelta
from django.utils import timezone


class BookingViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = Account.objects.create_user(
            username="testuser", password="12345", is_staff=True
        )
        self.client.login(username="testuser", password="12345")
        self.film = film.objects.create(movie_name="Test Film")
        self.show = show.objects.create(
            movie=self.film,
            start_date=datetime.now(timezone.utc),
            end_date=datetime.now(timezone.utc) + timedelta(days=1),
            price=100,
            showtime=datetime.now(timezone.utc).time(),
        )
        self.booking = booking.objects.create(
            user=self.user,
            show=self.show,
            seat_num="A1",
            num_seats=1,
            total=100,
            show_date=datetime.now(timezone.utc).date(),
            booked_date=datetime.now(timezone.utc),
        )

    def test_index_view(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "dashboard.html")
        self.assertIn("graph1", response.context)
        self.assertIn("graph2", response.context)
        self.assertIn("tabledata", response.context)
        self.assertIn("movies_count", response.context)
        self.assertIn("users_count", response.context)
        self.assertIn("bookings_count", response.context)

    def test_movies_view(self):
        response = self.client.get(reverse("movies"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "movies.html")
        self.assertIn("film_list", response.context)

    def test_banners_view(self):
        response = self.client.get(reverse("banners"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "banners.html")
        self.assertIn("banners", response.context)

    def test_shows_view(self):
        response = self.client.get(reverse("shows"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "shows.html")
        self.assertIn("shows", response.context)

    def test_users_view(self):
        response = self.client.get(reverse("users"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users.html")
        self.assertIn("users", response.context)

    def test_create_film(self):
        film_count = film.objects.count()
        new_film = film.objects.create(movie_name="New Test Film")
        self.assertEqual(film.objects.count(), film_count + 1)
        self.assertEqual(new_film.movie_name, "New Test Film")

    def test_create_show(self):
        show_count = show.objects.count()
        new_show = show.objects.create(
            movie=self.film,
            start_date=datetime.now(timezone.utc),
            end_date=datetime.now(timezone.utc) + timedelta(days=1),
            price=150,
            showtime=datetime.now(timezone.utc).time(),
        )
        self.assertEqual(show.objects.count(), show_count + 1)
        self.assertEqual(new_show.price, 150)

    def test_create_banner(self):
        banner_count = banner.objects.count()
        new_banner = banner.objects.create(
            movie=self.film, url="http://example.com/banner.jpg"
        )
        self.assertEqual(banner.objects.count(), banner_count + 1)
        self.assertEqual(new_banner.url, "http://example.com/banner.jpg")
