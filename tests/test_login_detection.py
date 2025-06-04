import unittest
from app import app

class FlaskLoginTestCase(unittest.TestCase):
    def setUp(self):
        # Create a test client
        self.app = app.test_client()
        self.app.testing = True

    def test_login_page_loads(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Login', response.data)

    def test_login_valid_user(self):
        # Simulate login with known valid credentials (from users.db)
        response = self.app.post('/', data=dict(
            email='user01@mh-cybersolutions.de',
            password='pass01',
            screen_resolution='1366x768'
        ), follow_redirects=True)
        self.assertIn(b'dashboard', response.data.lower())

    def test_login_invalid_user(self):
        response = self.app.post('/', data=dict(
            email='fake@mh-cybersolutions.de',
            password='wrongpass',
            screen_resolution='1024x768'
        ), follow_redirects=True)
        self.assertIn(b'login failed', response.data.lower())

if __name__ == '__main__':
    unittest.main()
