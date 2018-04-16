from django.test import TestCase
from django.urls import resolve
from accounts.views import profile, register, login, logout

class TestAccountsPage(TestCase):
    
    # def test_profile_url_returns_ok(self):
    #     response = self.client.get("/accounts/profile/")
    #     self.assertEqual(response.status_code, 200)
    def test_profile_url_resolves_to_profile_view(self):
        found = resolve('/accounts/profile/')  
        self.assertEqual(found.func, profile)
        
    def test_register_url_returns_ok(self):
        response = self.client.get("/accounts/register/")
        self.assertEqual(response.status_code, 200)
    def test_register_url_resolves_to_register_view(self):
        found = resolve('/accounts/register/')  
        self.assertEqual(found.func, register)
        
    def test_login_url_returns_ok(self):
        response = self.client.get("/accounts/login/")
        self.assertEqual(response.status_code, 200)
    def test_login_url_resolves_to_login_view(self):
        found = resolve('/accounts/login/')  
        self.assertEqual(found.func, login)
        
    def test_logout_url_returns_ok(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    def test_logout_url_resolves_to_logout_view(self):
        found = resolve('/accounts/logout/')  
        self.assertEqual(found.func, logout)