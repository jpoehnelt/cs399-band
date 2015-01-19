from django.test import Client, TestCase
from django.core.urlresolvers import reverse
from django.contrib.staticfiles import finders
from app.settings import BASE_DIR

class TestViews(TestCase):
    """
    Use the test client to get all of the views and test that the correct template was used.
    """
    def test_home(self):
        url = reverse('home')
        self.assertEqual(url, '/')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_discography(self):
        url = reverse('discography')
        self.assertEqual(url, '/discography')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'discography.html')

    def test_members(self):
        url = reverse('members')
        self.assertEqual(url, '/members')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'members.html')

    def test_tour(self):
        url = reverse('tour')
        self.assertEqual(url, '/tour')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tour.html')

    def test_static_config(self):
        """
        Tests the static file configuration to make sure
        that the app looks in the static folder.
        """
        result = finders.find('dummy_filename')
        searched_locations = finders.searched_locations
        self.assertIn(BASE_DIR+'/app/static', searched_locations)



