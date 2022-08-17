from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


# Create your tests here.

# test with all parameters
# test without day parameter
# test with invalid day parameter
# test with invalid city

class TestWeatherAPI(APITestCase):
    def setUp(self) -> None:
        self.base_url = reverse('temperature-info', kwargs={"city": "London"})
        self.days_params = {'days': 3}

    def test_fetch_compute_temp_stats(self) -> None:
        """
            All parameters are present
        """
        response = self.client.get(self.base_url, self.days_params, format='json')
        data = response.data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('maximum', data)
        self.assertIn('minimum', data)
        self.assertIn('average', data)
        self.assertIn('days', data)
        self.assertIn('city', data)

    def test_fetch_without_day_param(self) -> None:
        """
               Day query parameter is omitted from the request
        """
        response = self.client.get(self.base_url, format='json')
        data = response.data
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('days parameter is missing', data)

    def test_fetch_with_invalid_city(self) -> None:
        """
               An invalid city is passed to the base url
        """
        self.base_url = reverse('temperature-info', kwargs={"city": "NonExistent"})
        response = self.client.get(self.base_url, self.days_params, format='json')
        data = response.data
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual('No matching location found.', data)
