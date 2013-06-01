from mrjob.job import MRJob


class MRWordCountJob(MRJob):

    def mapper(self, _, line):
        # does not count newlines
        yield 'characters', len(line)
        yield 'words', sum(1 for word in line.split() if word.strip())
        yield 'lines', 1

    def reducer(self, key, values):
        yield(key, sum(values))


if __name__ == '__main__':
    MRWordCountJob.run()
