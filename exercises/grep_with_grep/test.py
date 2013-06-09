import unittest

from grep_job import MRGrepJob


CORRECT_ANSWER = {
    'Stella Soto',
    'Stefany Mclean',
    'Steven Butler',
    'Stephanie Martin',
}


class TestGrep(unittest.TestCase):

    def setUp(self):
        self.input_path = 'data/names.txt'

    def _test_with_args(self, args):
        mr_job = MRGrepJob(['--runner=local', self.input_path] + args)

        with mr_job.make_runner() as runner:
            runner.run()
            self.assertEqual(
                set(mr_job.parse_output_line(line)[1].rstrip()
                    for line in runner.stream_output()),
                CORRECT_ANSWER)

    def test_basic(self):
        self._test_with_args(['-e', r'\^Ste\.\*'])

    def test_extended(self):
        self._test_with_args(['-e', r'^Ste.*', '--extended'])


if __name__ == '__main__':
    unittest.main()
