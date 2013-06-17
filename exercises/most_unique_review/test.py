import unittest

from unique_review_job import MRUniqueReviewJob


CORRECT_ANSWER = "FCcFT610nQBVcRdY-devQA:40aklZ2SQPKnlTPZdvAqww:2012-01-14\n"


class TestUniqueReviewJob(unittest.TestCase):

    def setUp(self):
        self.short_text_input = 'data/yelp/reviews_100.json'

    def test_job(self):
        mr_job = MRUniqueReviewJob(['--runner=inline', self.short_text_input])

        with mr_job.make_runner() as runner:
            runner.run()
            for line in runner.stream_output():
                self.assertEqual(line, CORRECT_ANSWER)


if __name__ == '__main__':
    unittest.main()
