from django.contrib.auth.decorators import login_required
from django.test import TestCase
from django.urls import reverse

class BaseTest(TestCase):
    def setUp(self):
        self.register_url = reverse('portfolio-register')
        self.profile_url = reverse('portfolio-profile')
        self.user={
            'email' : 'testemail@gmail.com',
            'username' : 'username',
            'password1' : 'WdW123456',
            'password2' : 'WdW123456',
        }
        
        return super().setUp()


class RegisterTest(BaseTest):
    def test_can_view_page_correctly(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'users/register.html')

    def test_can_register_user(self):
        response = self.client.post(self.register_url, self.user, format='text/html')
        self.assertEqual(response.status_code,302)




