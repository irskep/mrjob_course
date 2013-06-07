import unittest

from grep_job import MRGrepJob


CORRECT_ANSWER = {
    'Stella Soto',
    'Stefany Mclean',
    'Steven Butler',
    'Stephanie Martin',
}


class TestWordCount(unittest.TestCase):

    def setUp(self):
        self.input_path = 'data/names.txt'

    def test_wc(self):
        mr_job = MRGrepJob(['--runner=inline', '-e', '^Ste.*',
                            self.input_path])

        with mr_job.make_runner() as runner:
            runner.run()
            self.assertEqual(
                set(mr_job.parse_output_line(line)[1].rstrip()
                    for line in runner.stream_output()),
                CORRECT_ANSWER)


if __name__ == '__main__':
    unittest.main()
