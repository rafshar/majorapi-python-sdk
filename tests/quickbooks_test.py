import unittest
from .context import majorapi


class MajorApiQuickbooksTest(unittest.TestCase):
    def test_creating_customer_requires_configured_url(self):
        api = majorapi.MajorApiQuickbooks('username', 'apikey')
        self.assertRaises(MajorApiError, api.create_customer, {'name': 'John Smith'})

    def test_creating_customer_requires_no_errors(self):
        api = majorapi.MajorApiQuickbooks('username', 'apikey')
        self.assertRaises(MajorApiError, api.create_customer, {'name': 'This name is too long to be an acceptable customer name'})

if __name__ == '__main__':
    unittest.main()
