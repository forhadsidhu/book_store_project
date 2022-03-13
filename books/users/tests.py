from django.test import TestCase
from django.contrib.auth import get_user_model
from django.test import TestCase


class CustomUserTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        # creating user
        user = User.objects.create_user(
            username='will',
            email='will@gmail.com',
            password='testpass123'
        )
        # verifying user
        self.assertEqual(user.username, 'will')
        self.assertEqual(user.email, 'will@gmail.com')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        # creating user
        admin_user = User.objects.create_superuser(
            username='forhad',
            email='forhad@gmail.com',
            password='forhard123'
        )
        # verifying user
        self.assertEqual(admin_user.username, 'forhad')
        self.assertEqual(admin_user.email, 'forhad@gmail.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
