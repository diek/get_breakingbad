import unittest

import requests

from get_scripts import generate_urls

EPISODES = [7, 13, 13, 13, 16]
TEST_URL = 'http://www.springfieldspringfield.co.uk/view_episode_scripts.php?tv-show=breaking-bad&episode='


class TestResponse(unittest.TestCase):

    def test_generate_urls(self):
        """Total episodes = 62
        """
        res = generate_urls(EPISODES, TEST_URL)
        self.assertEqual(len(res), sum(EPISODES))

    def test_response(self):
        """Ensure response 200
        """
        urls = generate_urls(EPISODES, TEST_URL)
        for k, v in urls.items():
            res = requests.get(v)
            self.assertEqual(res.status_code, 200)


if __name__ == '__main__':
    unittest.main()
