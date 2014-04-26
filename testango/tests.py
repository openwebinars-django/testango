from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client


class TestangoTestCase(TestCase):

    def setUp(self):
        self.client = Client(enforce_csrf_checks=False)

    def testango_word(self):
        word = 'hello'
        url = reverse('word_view', args=(word,))
        response = self.client.get(url)
        self.assertEqual(response.content, word)
        self.assertNotEqual(response.content, 'bye')