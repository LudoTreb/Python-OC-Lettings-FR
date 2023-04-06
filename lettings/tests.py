import pytest
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from lettings.models import Address, Letting


class LettingsPageTestCase(TestCase):
    def setUp(self):
        """ Configure the variables for the tests """

        self.good_url_index = reverse("lettings:index")
        self.good_address = Address.objects.create(
            number=50,
            street="test_street",
            city="test_city",
            state="test_state",
            zip_code=77777,
            country_iso_code="FR"
        )
        self.good_letting = Letting.objects.create(
            title="",
            address=self.good_address
        )
        self.good_url_letting = reverse("lettings:letting", args=[self.good_address.id])

    def test_is_good_lettings_page_index(self):
        """ Test lettings index page good path """

        response = self.client.get(self.good_url_index)
        self.assertContains(response, "<h1>Lettings</h1>", status_code=200)