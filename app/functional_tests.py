import unittest
from unittest import TestCase, mock
from scraper_service import app, http_get

class TestScrapeEndpoint(TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_scrape_endpoint_missing_url(self):
        response = self.app.post('/', json={})
        self.assertEqual(response.status_code, 400)
        self.assertIn('Missing URL', response.get_json()['error'])

    @mock.patch('scraper_service.http_get.labels')
    def test_scrape_valid_url(self, mock_labels):
        mock_labels.return_value.get.return_value = 1
        response = self.app.post('/', json={'url': 'http://phaidra.ai'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(mock_labels.call_args[0][0], 'http://phaidra.ai')
        self.assertEqual(mock_labels.call_args[0][1], '200')

    def test_scrape_endpoint_invalid_url(self):
       response = self.app.post('/', json={'url': 'http://invalid-url'})
       self.assertEqual(response.status_code, 500)
       self.assertIn('Could not resolve host', response.get_json()['error'])

if __name__ == '__main__':
    unittest.main()
