import unittest

from wfc_job import MRWordFrequencyCountJob


# only check words with over 100 occurrences
CORRECT_ANSWER = {
    'a': 167,
    'all': 108,
    'and': 611,
    'any': 127,
    'as': 148,
    'be': 289,
    'by': 172,
    'for': 205,
    'from': 103,
    'have': 159,
    'his': 144,
    'in': 287,
    'of': 831,
    'or': 317,
    'our': 264,
    'shall': 319,
    'that': 136,
    'the': 997,
    'to': 456,
    'we': 178,
    'will': 104,
}


class TestWordFrequencyCount(unittest.TestCase):

    def setUp(self):
        self.short_text_input = 'data/magna_carta.txt'

    def test_wc(self):
        mr_job = MRWordFrequencyCountJob(
                ['--runner=inline', self.short_text_input])

        with mr_job.make_runner() as runner:
            runner.run()
            values = {key: 0 for key in CORRECT_ANSWER}
            for line in runner.stream_output():
                key, value = mr_job.parse_output_line(line)
                if key in CORRECT_ANSWER:
                    # ensure key only appears once
                    self.assertEqual(values[key], 0)
                    values[key] = value
            # check relevant values
            self.assertEqual(values, CORRECT_ANSWER)


if __name__ == '__main__':
    unittest.main()
