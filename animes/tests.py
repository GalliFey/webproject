from django.test import TestCase, Client


class AllCaseTest(TestCase):
    def setUp(self):
        self.client = Client()


    def test_urls(self):
        response = self.client.get('/filter/')
        self.assertEqual(response.status_code, 200)
