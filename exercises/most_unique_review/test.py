import unittest

from unique_review_job import MRUniqueReviewJob


CORRECT_ANSWER = "81IjU5L-t-QQwsE38C63hQ:OlMjqqzWZUv2-62CSqKq_A:2008-07-02\n"


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
