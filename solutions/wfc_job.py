"""
Write a job that calculates the number of occurrences of individual words in
the input text. The job should output one key/value pair per word where the key
is the word and the value is the number of occurrences.
"""
from collections import Counter, defaultdict
from mrjob.job import MRJob


class MRWordFrequencyCountJob(MRJob):

    def steps(self):
        return [self.mr(mapper_init=self.mapper_init, mapper=self.mapper,
                        mapper_final=self.mapper_final,
                        combiner=self.sum_words, reducer=self.sum_words)]

    def mapper_init(self):
        #self.words = {}
        #self.words = defaultdict(0)
        #self.words = defaultdict(lambda: 0)
        self.words = Counter()

    def mapper(self, _, line):
        for word in line.split():
            if word.strip():
                #self.words.setdefault(word, 0)

                #if word not in words:
                #    words[word] = 0

                #self.words[word] = self.words.get(word, 0) + 1

                self.words[word] += 1

    def mapper_final(self):
        for word, count in self.words.iteritems():
            yield word, count

    def sum_words(self, key, values):
        yield key, sum(values)


if __name__ == '__main__':
    MRWordFrequencyCountJob.run()
