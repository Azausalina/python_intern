"""
app tests example

"""

from app.main import is_alive_host

import unittest

class TestIsAliveHostMethod(unittest.TestCase):

    def test_alive_host(self):
        self.assertTrue(is_alive_host('http://google.com'))

    def test_hostname_without_http(self):
        self.assertTrue(is_alive_host('google.com'))

    def test_hostname_with_https(self):
        self.assertTrue(is_alive_host('https://pythonworld.ru'))

    def test_down_host(self):
        self.assertFalse(is_alive_host('http://googl1e.com'))

    def test_type_hostname(self):
        with self.assertRaises(TypeError) as context:
            is_alive_host(42)
        self.assertTrue("hostname must be str not" in str(context.exception))


if __name__ == "__main__":
    unittest.main()
