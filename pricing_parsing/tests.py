# from django.test import TestCase
# from django.test import TestCase, TransactionTestCase
# from django.urls import reverse
# from django.test.client import Client
# from django.contrib.auth.models import User
# from rest_framework import status
# from rest_framework.test import APITestCase, APIRequestFactory, APIClient
# import json

# # Create your tests here.


# class MovplncmpcalTest(APITestCase):
# 		databases = '__all__'

# 		def setUp(self):
# 				User.objects.create_user('eurico', password='tangoteste')

# 		def test_consumo_de_dados_de_movplncmpcal(self):
# 			"""

# 			checa o retorno e paginação de movplncmpcal

# 			""" 
# 			self.client.login(username='eurico', password='tangoteste')
# 			response = self.client.get('/api/pricing_parsing/movplncmpcal/?page_size=9&page=3', format='json')
# 			self.assertEqual(json.loads(response.content), [])
# 			self.assertEqual(len(json.loads(response.content)), 6)
