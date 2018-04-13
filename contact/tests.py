from django.test import TestCase
from django.urls import resolve
from contact.views import contactform, thanks

# Create your tests here.

class TestContactPage(TestCase):
    
    def test_contact_url_returns_ok(self):
        response = self.client.get("/contact/")
        self.assertEqual(response.status_code, 200)
    def test_contact_url_resolves_to_contact_view(self):
        found = resolve('/contact/')  
        self.assertEqual(found.func, contactform)
        
    def test_contact_thanks_url_returns_ok(self):
        response = self.client.get("/contact/thanks/")
        self.assertEqual(response.status_code, 200)
    def test_contact_thanks_url_resolves_to_contact_thanks_view(self):
        found = resolve('/contact/thanks/')  
        self.assertEqual(found.func, thanks)
