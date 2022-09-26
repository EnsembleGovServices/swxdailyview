from application import application
import unittest


class FlaskTest(unittest.TestCase):

    def test_index(self):
        tester = application.test_client(self)
        response = tester.get('/')
        status_code = response.status_code
        self.assertEqual(status_code, 200)


class Sec(unittest.TestCase):
    def test_kp_current(self):
        tester = application.test_client(self)
        response = tester.get('/current-kp-index')
        status_code = response.status_code
        self.assertEqual(status_code, 200)


class Third(unittest.TestCase):
    def test_interval_kp(self):
        tester = application.test_client(self)
        response = tester.get('/get-interval-kp-data')
        status_code = response.status_code
        self.assertEqual(status_code, 200)


class For(unittest.TestCase):
    def test_predicted_kp(self):
        tester = application.test_client(self)
        response = tester.get('/predicted-kp-index')
        status_code = response.status_code
        self.assertEqual(status_code, 200)


if __name__ == "__main__":
    unittest.main()
