import json
import os

from dotenv import load_dotenv
from django.test import TestCase, Client

from .models import CustomUser, Task

load_dotenv()

"""
We load from the .env file, constants in order to create a user in our test database
"""
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("password")
FIRSTNAME = os.getenv("FIRSTNAME")
LASTNAME = os.getenv("LASTNAME")


class UserModelTest(TestCase):
    def setUp(self):
        CustomUser.objects.create(email=EMAIL,
                                  password=PASSWORD,
                                  first_name=FIRSTNAME,
                                  last_name=LASTNAME)
        self.client = Client(enforce_csrf_checks=False)

    def test_user_added(self):
        user_test = CustomUser.objects.get(email=EMAIL)

        # Testing that the user is added in BDD with all of his information
        self.assertEqual(user_test.email, "test1@gmail.com")
        self.assertEqual(user_test.first_name, "User")
        self.assertEqual(user_test.last_name, "Test")
        self.assertFalse(user_test.is_admin)  # A user is not an admin

    def test_user_authenticate(self):
        user_test = CustomUser.objects.get(email=EMAIL)
        data = {'email': EMAIL, 'password': PASSWORD}
        c = self.client.post(path='/login_user', data=data, content_type="application/json")
        self.assertEqual(c.status_code, 200)


class TaskModelTest(TestCase):
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


"""
Testing the API 
"""
class TestTaskAPI(TestCase):
    def setUp(self):
        self.client = Client(enforce_csrf_checks=False)
        self.user = CustomUser.objects.create(email=EMAIL,
                                              password=PASSWORD,
                                              first_name=FIRSTNAME,
                                              last_name=LASTNAME)

        # adding a task
        self.task1 = Task.objects.create(description="Premier test", created_by=self.user)
        self.task2 = Task.objects.create(description="Premier test", created_by=self.user)
        self.task3 = Task.objects.create(description="Premier test", created_by=self.user)

    def test_get_tasks(self):
        response = self.client.get('/getTasks')
        self.assertEqual(response.status_code, 200)
        response_json = json.loads(response.content)




