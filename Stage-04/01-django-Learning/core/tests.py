from django.test import TestCase


# TestCase is Django's built-in class for writing and running tests.
# By inheriting from TestCase, we get useful testing features such as
# self.client for sending requests to our Django application.
class testCoreApp(TestCase):

    # Test whether the Home page is working correctly.
    def test_home_page(self):

        # self.client acts like a small browser for testing.
        # .get('/') sends a GET request to the Home URL.
        # The response from Django is stored in the 'response' variable.
        response = self.client.get('/')

        # Check whether Django returned HTTP status code 200.
        # 200 means the request was successful.
        # If the value is not 200, this test will fail.
        self.assertEqual(response.status_code, 200)


    # Test whether the About page contains the expected text.
    def test_about_page(self):

        # Use Django's test client to send a GET request to /about/.
        response = self.client.get('/about/')

        # Check whether "about page" exists inside the response content.
        # If the text is not found, the test will fail.
        self.assertContains(response, "about page")