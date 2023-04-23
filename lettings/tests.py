from django.test import TestCase
from django.urls import reverse

from lettings.models import Address, Letting


class LettingsPageTestCase(TestCase):
    def setUp(self):
        """ All variables for the tests """

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
            title="title_letting",
            address=self.good_address
        )
        self.good_url_letting = reverse("lettings:letting", args=[self.good_address.id])

    def test_is_good_lettings_page_index(self):
        """ Test lettings index page good path """

        response = self.client.get(self.good_url_index)
        self.assertContains(response, "<h1>Lettings</h1>", status_code=200)

    def test_is_good_letting_page(self):
        """Test letting page good path"""
        response = self.client.get(self.good_url_letting)
        self.assertContains(response, "<h1>title_letting</h1>", status_code=200)

    def test_is_good_letting_display(self):
        """ Test a letting page display """

        response = self.client.get(self.good_url_letting)
        self.assertContains(response, "50 test_street", status_code=200)
        self.assertContains(response, "test_city, test_state 77777", status_code=200)
        self.assertContains(response, "FR", status_code=200)

    def test_is_good_lettings_display(self):
        """..."""

        response = self.client.get(self.good_url_index)
        self.assertContains(response, "href", count=3, status_code=200)


class LettingsPageEmptyTestCase(TestCase):
    def setUp(self):
        """All variables for the tests"""
        self.good_url_index = reverse("lettings:index")

    def test_if_lettings_page_have_no_lettings(self):
        """Test if lettings index page have lettings"""
        response = self.client.get(self.good_url_index)
        self.assertContains(response, "No lettings are available", status_code=200)
