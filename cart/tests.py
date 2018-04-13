from django.test import TestCase
from django.urls import resolve
from cart.views import view_cart, add_to_cart, remove_from_cart
from products.views import listcoffee

# Create your tests here.

class TestCartPage(TestCase):
    
    def test_view_cart_url_returns_ok(self):
        response = self.client.get("/cart/view/")
        self.assertEqual(response.status_code, 200)
    def test_view_cart_url_resolves_to_view_cart_view(self):
        found = resolve('/cart/view/')  
        self.assertEqual(found.func, view_cart)
        
    def test_add_to_cart_url_returns_ok(self):
        response = self.client.get("/products/")
        self.assertEqual(response.status_code, 200)
    def test_add_to_cart_url_resolves_to_add_to_cart_view(self):
        found = resolve('/products/')  
        self.assertEqual(found.func, listcoffee)
        
    def test_remove_from_cart_url_returns_ok(self):
        response = self.client.get("/cart/view/")
        self.assertEqual(response.status_code, 200)
    def test_remove_from_cart_url_resolves_to_remove_from_cart_view(self):
        found = resolve('/cart/view/')  
        self.assertEqual(found.func, view_cart)