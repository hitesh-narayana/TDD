from django.test import TestCase

# Create your tests here.

class ListViewTest(TestCase):

    def test_uses_list_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'list.html')