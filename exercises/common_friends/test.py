import unittest
from StringIO import StringIO

from compute_common_friends import compute_common_friends


CORRECT_ANSWER = {
    'Steve Johnson': {
        'Fred Hatfull': 1,
        'Tim Henderson': 0,
        'Toby Waite': 1,
    },
    'Fred Hatfull': {
        'Steve Johnson': 1,
        'Toby Waite': 1,
    },
    'Toby Waite': {
        'Steve Johnson': 1,
        'Fred Hatfull': 1,
    },
    'Tim Henderson': {
        'Steve Johnson': 0,
    },
}


class TestCommonFriends(unittest.TestCase):

    def setUp(self):
        self.short_text_input = 'data/friends_test.txt'

    def test(self):
        self.assertEqual(
            compute_common_friends([self.short_text_input]), CORRECT_ANSWER)


if __name__ == '__main__':
    unittest.main()
