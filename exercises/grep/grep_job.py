"""
Filter input lines by Python regular expression. The expression to use should
be supplied by the command line argument -e or --expression.

Example input:

    abc
    aaabb
    acca

Run with:

    python grep_job.py -e '^a.*b$'

Output:

    abc

We are using a flag (-e) instead of a positional argument because mrjob does
not provide a straightforward way to do that.
"""

from mrjob.job import MRJob


class MRGrepJob(MRJob):

    def mapper(self, _, line):
        yield None, line


if __name__ == '__main__':
    MRGrepJob.run()
