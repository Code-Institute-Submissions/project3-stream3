from django.test import TestCase
from django.urls import resolve
from products.views import listcoffee, detailcoffee

# Create your tests here.

class TestProductsPage(TestCase):
        
    def test_products_url_returns_ok(self):
        response = self.client.get("/products/")
        self.assertEqual(response.status_code, 200)
    def test_root_url_resolves_to_products_view(self):
        found = resolve('/')  
        self.assertEqual(found.func, listcoffee)
    
    # def test_products_id_url_returns_ok(self):
    #     response = self.client.get("/products/1")
    #     self.assertEqual(response.status_code, 200)
    def test_product_id_url_resolves_to_products_id_view(self):
        found = resolve('/products/1')
        self.assertEqual(found.func, detailcoffee)
