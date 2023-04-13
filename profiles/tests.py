from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from profiles.models import Profile

# Create your tests here.
import pytest


# @pytest.mark.django_db
# class TestProfile:
#
#     def test_create_profile(self):
#         profile = Profile.objects.create(user=User.objects.create_user("me", "meme", "me@me.me"))
#         assert profile


class ProfilesPageTestCase(TestCase):

    def setUp(self):
        """ All variables for the tests """
        self.good_user = User.objects.create(username="test_ludo")
        self.good_profile = Profile.objects.create(user=self.good_user, favorite_city="test_city")
        self.good_url_index = reverse("profiles:index")
        self.good_url_profile = reverse("profiles:profile", args=[self.good_profile.user.username])

    def test_is_good_profiles_page_index(self):
        """..."""
        response = self.client.get(self.good_url_index)
        self.assertContains(response, "<h1>Profiles</h1>", status_code=200)

    def test_is_good_profile_page(self):
        """..."""
        response = self.client.get(self.good_url_profile)
        self.assertContains(response, "<h1>test_ludo</h1>", status_code=200)

    def test_is_good_profile_display(self):
        """..."""
        response = self.client.get(self.good_url_profile)
        self.assertContains(response, "Favorite city: test_city", status_code=200)


class ProfilesPageEmptyTestCase(TestCase):
    def setUp(self):
        """ All variables for the tests """
        self.good_url_index = reverse("profiles:index")

    def test_if_profiles_page_have_no_profile(self):
        """..."""
        response = self.client.get(self.good_url_index)
        self.assertContains(response, "No profiles are available", status_code=200)

