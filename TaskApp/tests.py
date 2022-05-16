import os

from dotenv import load_dotenv
from django.test import TestCase
from .models import CustomUser, Task

load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("password")
FIRSTNAME = os.getenv("FIRSTNAME")
LASTNAME = os.getenv("LASTNAME")


class TestUser(TestCase):
    def setUp(self):
        CustomUser.objects.create(email=EMAIL,
                                  password=PASSWORD,
                                  first_name=FIRSTNAME,
                                  last_name=LASTNAME)

    def test_user_added(self):
        user_test = CustomUser.objects.get(email=EMAIL)

        # Testing that the user is added in BDD with all of his information
        self.assertEqual(user_test.email, "test1@gmail.com")
        self.assertEqual(user_test.first_name, "User")
        self.assertEqual(user_test.last_name, "Test")
        self.assertFalse(user_test.is_admin)


class TestTask(TestCase):
    def setUp(self):
        # Adding a fake user
        self.user = CustomUser.objects.create(email=EMAIL,
                                              password=PASSWORD,
                                              first_name=FIRSTNAME,
                                              last_name=LASTNAME)

        # adding a task
        self.task = Task.objects.create(description="Premier test", created_by=self.user)

    def test_task_created(self):
        self.assertEqual(self.task.description, "Premier test")
        self.assertEqual(self.task.created_by, self.user)

    def test_task_is_not_completed(self):
        # By default, every new added task is not completed
        self.assertFalse(self.task.is_completed)
