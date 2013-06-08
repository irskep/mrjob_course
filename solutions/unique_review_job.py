"""
Find the review with the most unique words (i.e. words used in no other
reviews). Output the review's ID (see ``review_id`` below). In the case of a
tie, output both review IDs.

So if review A has the words "map map map reduce reduce" and review B has the
words "map combine combine reduce" then the output should be 'B' because it has
one unique word.

Hint: there will be three map/reduce steps.
"""
from mrjob.job import MRJob
from mrjob.protocol import (
    JSONValueProtocol,
    RawValueProtocol,
)


def review_id(obj):
    return "%s:%s:%s" % (obj['business_id'], obj['user_id'], obj['date'])


class MRUniqueReviewJob(MRJob):

    INPUT_PROTOCOL = JSONValueProtocol
    OUTPUT_PROTOCOL = RawValueProtocol

    def steps(self):
        return [self.mr(mapper=self.mapper_review_words,
                        reducer=self.reducer_unique_words),
                self.mr(reducer=self.reducer_unique_word_count),
                self.mr(reducer=self.reducer_max_unique_words)]

    def mapper_review_words(self, _, obj):
        if obj['type'] == 'review':
            for word in obj['text'].split():
                if word.strip():
                    yield word, review_id(obj)

    def reducer_unique_words(self, word, review_ids):
        review_ids = list(review_ids)
        if len(set(review_ids)) == 1:
            yield review_ids[0], word

    def reducer_unique_word_count(self, review_id, words):
        yield None, [review_id, len(set(list(words)))]

    def reducer_max_unique_words(self, _, values):
        max_count = 0
        review_ids = []
        for review_id, num_words in values:
            if num_words > max_count:
                max_count = num_words
                review_ids = []
            if num_words == max_count:
                review_ids.append(review_id)
        for review_id in review_ids:
            yield None, review_id


if __name__ == '__main__':
    MRUniqueReviewJob.run()
