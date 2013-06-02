import unittest
from StringIO import StringIO

from most_used_words_job import MRMostUsedWordsByLengthJob


input_text = """better babies build better blogs\n"""

CORRECT_ANSWER = {
    6: {'better'},
    5: {'build', 'blogs'},
}


class TestMostUsedWords(unittest.TestCase):

    def test_wc(self):
        mr_job = MRMostUsedWordsByLengthJob(
                ['--runner=inline', '-'])
        mr_job.sandbox(stdin=StringIO(input_text))

        with mr_job.make_runner() as runner:
            runner.run()
            for line in runner.stream_output():
                key, value = mr_job.parse_output_line(line)
                self.assertEqual(set(value), CORRECT_ANSWER[key])


if __name__ == '__main__':
    unittest.main()
