from django.test import TestCase
from .models import CustomUser, Task


class TestUser(TestCase):
    def setUp(self):
        CustomUser.objects.create(email="test1@gmail.com", password="mypassword", first_name="User", last_name="Test")

    def test_user_added(self):
        user_test = CustomUser.objects.get(email="test1@gmail.com")

        # Testing that the user is added in BDD with all of his information
        self.assertEqual(user_test.email, "test1@gmail.com")
        self.assertEqual(user_test.first_name, "User")
        self.assertEqual(user_test.last_name, "Test")
        self.assertFalse(user_test.is_admin)

