"""
Calculate the number of characters, words, and lines in the given input. Output
will be similar (but not identical) to the UNIX ``wc`` utility.

The input will be UTF-8 text files. The job should output three keys:
'characters', 'words', and 'lines'.

The character count does not include newlines. A word is any sequence of
non-whitespace characters of nonzero length.

Your output will be different from that of the ``wc`` utility due to the way
newlines and words are calculated.

Run your job from the command line like this:

    python exercises/wc/wc_job.py data/magna_carta.txt --quiet

or run the test cases like this:

    python exercises/wc/test.py
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
