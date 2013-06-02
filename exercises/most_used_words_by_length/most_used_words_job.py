"""
Calculate the most used word for each length of word. The output should be:

    <length of word>: <list of words that tie for most used word of that length>

For example, in the string "better babies build better blogs", the relevant
information is:

    word    length  # occurrences
    better  6       2
    babies  6       1
    build   5       1
    blogs   5       1

So the output would be:

    6: ['better']
    5: ['build', 'blogs']
"""

from mrjob.job import MRJob


def tokenize(line):
    """Yield each individual word in a line"""
    for word in line.split():
        if word.strip():
            yield word


class MRMostUsedWordsByLengthJob(MRJob):

    def steps(self):
        return [self.mr(mapper=self.mapper_count_words)]

    def mapper_count_words(self, _, line):
        for word in tokenize(line):
            yield word, 1


if __name__ == '__main__':
    MRMostUsedWordsByLengthJob.run()
