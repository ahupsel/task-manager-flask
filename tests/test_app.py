import unittest
import sys
import os

sys.path.insert(0, os.path.abspath("todo_project"))

from todo_project import app


class TestTaskManagerApp(unittest.TestCase):

    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    def test_home_page_status(self):
        response = self.client.get("/")
        self.assertIn(response.status_code, [200, 302])

    def test_login_page_status(self):
        response = self.client.get("/login")
        self.assertIn(response.status_code, [200, 302])

    def test_register_page_status(self):
        response = self.client.get("/register")
        self.assertIn(response.status_code, [200, 302])


if __name__ == "__main__":
    unittest.main()
