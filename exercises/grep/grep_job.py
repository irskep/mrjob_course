"""
Filter input lines by regular expression. The expression to use should be
supplied by the command line argument -e or --expression.

Example input:

    abc
    aaabb
    acca

Run with:

    python grep_job.py -e '^a.*b$'

Output:

    abc
"""

import re

from mrjob.job import MRJob
from mrjob.protocol import RawValueProtocol


class MRGrepJob(MRJob):

    INPUT_PROTOCOL = RawValueProtocol  # this is the default
    OUTPUT_PROTOCOL = RawValueProtocol

    def configure_options(self):
        super(MRGrepJob, self).configure_options()
        self.add_passthrough_option('-e', '--expression')

    def mapper_init(self):
        if self.options.expression:
            self.re = re.compile(self.options.expression)
        else:
            self.re = re.compile('.*')

    def mapper(self, _, line):
        if self.re.match(line):
            yield None, line


if __name__ == '__main__':
    MRGrepJob.run()
