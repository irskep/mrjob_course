"""
Write a job that calculates the most used word for each length of word. The
output should be:

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


def words(line):
    """Yield each individual word in a line"""
    for word in line.split():
        if word.strip():
            yield word


def find_max(word_count_pairs):
    """Given a list of (word, # occurrences of word in text) pairs, find the
    words that tie for the most occurrences in the text.
    """
    words = []
    max_count = 0
    for word, count in word_count_pairs:
        if count == max_count:
            words.append(word)
        elif count > max_count:
            words = [word]
            max_count = count
    return words


class MRMostUsedWordsByLengthJob(MRJob):

    def steps(self):
        return [
            self.mr(mapper=self.mapper_count_words,
                    reducer=self.reducer_sum_counts),
            self.mr(mapper=self.mapper_group_by_length,
                    reducer=self.reducer_find_max)
        ]

    # step 1: same as last exercise

    def mapper_count_words(self, _, line):
        for word in words(line):
            yield word, 1

    def reducer_sum_counts(self, key, values):
        yield key, sum(values)

    def mapper_group_by_length(self, key, value):
        yield len(key), [key, value]

    def reducer_find_max(self, key, values):
        yield key, find_max(values)


if __name__ == '__main__':
    MRMostUsedWordsByLengthJob.run()
