from django.test import TestCase
from django.urls import resolve
from products.views import listcoffee
from home.views import home, about, hours

class TestHomePage(TestCase):
    
    # home root and products link to the same view "listcoffee" (see first 4 tests)
    
    def test_root_url_returns_ok(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    def test_root_url_resolves_to_home_view(self):
        found = resolve('/')  
        self.assertEqual(found.func, listcoffee)
        
    def test_about_url_returns_ok(self):
        response = self.client.get("/about")
        self.assertEqual(response.status_code, 200)
    def test_about_url_resolves_to_about_view(self):
        found = resolve('/about')  
        self.assertEqual(found.func, about)
        
    def test_hours_url_returns_ok(self):
        response = self.client.get("/hours")
        self.assertEqual(response.status_code, 200)
    def test_hours_url_resolves_to_hours_view(self):
        found = resolve('/hours')  
        self.assertEqual(found.func, hours)

    


