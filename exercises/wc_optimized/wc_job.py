"""
Use ``mapper_init()`` and ``mapper_final()`` to write a more efficient version
of the wc exercise.
"""

from mrjob.job import MRJob


class MRWordCountJob(MRJob):

    def mapper(self, _, line):
        yield 'characters', 0
        yield 'words', 0
        yield 'lines', 0

    def reducer(self, key, values):
        yield key, 0


if __name__ == '__main__':
    MRWordCountJob.run()
