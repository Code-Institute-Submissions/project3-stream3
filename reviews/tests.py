from django.test import TestCase
from django.urls import resolve
from reviews.views import add_a_review

# Create your tests here.

class TestContactPage(TestCase):
    
    # def test_add_a_review_url_returns_ok(self):
    #     response = self.client.get("/products/1/")
    #     self.assertEqual(response.status_code, 200)
    def test_add_a_review_url_resolves_to_add_a_review_view(self):
        found = resolve('/reviews/add/')  
        self.assertEqual(found.func, add_a_review)
