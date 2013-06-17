"""
Use ``combiner()`` to optimize the word count job even more.
"""

from mrjob.job import MRJob


class MRWordCountJob(MRJob):

    def mapper_init(self):
        self.chars = 0
        self.words = 0
        self.lines = 0

    def mapper(self, _, line):
        self.chars += len(line)
        self.words += sum(1 for word in line.split() if word.strip())
        self.lines += 1

    def mapper_final(self):
        yield 'characters', self.chars
        yield 'words', self.words
        yield 'lines', self.lines

    def combiner(self, key, values):
        yield key, sum(values)

    def reducer(self, key, values):
        yield key, sum(values)


if __name__ == '__main__':
    MRWordCountJob.run()
