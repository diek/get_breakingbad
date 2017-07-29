import unittest

import requests

from get_scripts import generate_urls


class TestResponse(unittest.TestCase):
    TEST_URL = 'http://www.springfieldspringfield.co.uk/view_episode_scripts.php?tv-show=breaking-bad&episode='
    """
    Our basic test class
    """
    def test_generate_urls(self):


    def test_response(self):
        """
        Ensure response 200
        """
        res = requests.get(self.TEST_URL + 's01e01')
        print(res.status_code)
        self.assertEqual(res.status_code, 200)


if __name__ == '__main__':
    unittest.main()
