from django.test import TestCase
from django.contrib.auth.models import User

from profiles.models import Profile

# Create your tests here.
import pytest


@pytest.mark.django_db
class TestProfile:

    def test_create_profile(self):
        profile = Profile.objects.create(user=User.objects.create_user("me", "meme", "me@me.me"))
        assert profile
