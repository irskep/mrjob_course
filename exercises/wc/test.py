import unittest

from wc_job import MRWordCountJob


CORRECT_ANSWER = {
    'characters': 93116,
    'words': 16858,
    'lines': 1844,
}


class TestWordCount(unittest.TestCase):

    def setUp(self):
        self.short_text_input = u'data/magna_carta.txt'

    def test_wc(self):
        mr_job = MRWordCountJob(['--runner=inline', self.short_text_input])

        with mr_job.make_runner() as runner:
            runner.run()
            for line in runner.stream_output():
                key, value = mr_job.parse_output_line(line)
                self.assertEqual(value, CORRECT_ANSWER[key])

if __name__ == '__main__':
    unittest.main()
