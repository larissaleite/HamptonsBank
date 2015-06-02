import unittest, views

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = views.app.test_client()

    def test_index(self):
        rv = self.app.get('/')
        assert 'test fail' in rv.data

if __name__ == '__main__':
    unittest.main()