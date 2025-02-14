from django.test import TestCase
from .models import List
# Refactoring the functional test
from django.urls import reverse
from django.shortcuts import redirect

# Create your tests here.

class ListViewTest(TestCase):

    def test_uses_list_template(self):
        # response = self.client.get('/lists/')

        # Refactor
        response = self.client.get(reverse('view_list'))
        self.assertTemplateUsed(response, 'list.html')

    def test_can_save_a_POST_request(self):
        
        # self.client.post('/lists/', data={'name': 'A new list item'})
        # self.assertEqual(List.objects.count(), 1)
        # new_item = List.objects.first()
        # self.assertEqual(new_item.name, 'A new list item')

        # Refactor
        response = self.client.post(
            reverse('view_list'), 
            data={'name': 'A new list item'}
        )
        self.assertEqual(List.objects.count(), 1)
        new_item = List.objects.first()
        self.assertEqual(new_item.name, 'A new list item')
        self.assertRedirects(response, '/')