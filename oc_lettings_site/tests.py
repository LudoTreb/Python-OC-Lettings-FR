from django.test import TestCase
from django.urls import reverse


class HomePageTestCase(TestCase):
    def setUp(self):
        self.good_url = reverse("index")
        self.wrong_url = "/wrong_path"

    def test_is_good_home_page(self):
        """Test home page path is good"""
        response = self.client.get(self.good_url)
        self.assertContains(response, "<h1>Welcome to Holiday Homes</h1>", status_code=200)

    def test_is_not_home_page(self):
        """ Test home page wrong path"""
        response = self.client.get(self.wrong_url)
        assert response.status_code == 404
