import unittest
from app import app


class FlaskAppTestCases(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client() # create a client test
        self.app.testing = True # Enables app testing
    
    def test_home(self):
        response = self.app.get('/') # call the home route
        self.assertEqual(response.status_code, 200) #check status
        self.assertEqual(response.json['message'],  "Hello level 400 FET, Quality Assurance!") # Check response content

if __name__ == '__main__':
    unittest.main()