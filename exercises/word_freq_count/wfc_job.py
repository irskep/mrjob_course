"""
Calculate the number of occurrences of individual words in the input text. The
job should output one key/value pair per word where the key is the word and the
value is the number of occurrences.
"""

from mrjob.job import MRJob


class MRWordFrequencyCountJob(MRJob):

    def mapper(self, _, line):
        yield 'blah', 0

    def reducer(self, key, values):
        yield key, 0


if __name__ == '__main__':
    MRWordFrequencyCountJob.run()
