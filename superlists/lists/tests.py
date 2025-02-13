from django.test import TestCase

# Refactoring the functional test
from django.urls import reverse

# Create your tests here.

class ListViewTest(TestCase):

    def test_uses_list_template(self):
        # response = self.client.get('/lists/')

        # Refactor
        response = self.client.get(reverse('view_list'))
        self.assertTemplateUsed(response, 'list.html')