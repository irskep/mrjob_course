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

We are using a flag (-e) instead of a positional argument because mrjob does
not provide a straightforward way to do that.
"""

import re
from optparse import OptionError

from mrjob.job import MRJob
from mrjob.protocol import RawValueProtocol


class MRGrepJob(MRJob):

    INPUT_PROTOCOL = RawValueProtocol  # this is the default
    OUTPUT_PROTOCOL = RawValueProtocol

    def configure_options(self):
        super(MRGrepJob, self).configure_options()
        self.add_passthrough_option('-e', '--expression')

    def load_options(self, *args, **kwargs):
        super(MRGrepJob, self).load_options(*args, **kwargs)
        if not self.options.expression:
            raise OptionError("The -e flag is required.")

    def mapper_init(self):
        self.re = re.compile(self.options.expression)

    def mapper(self, _, line):
        if self.re and self.re.match(line):
            yield None, line


if __name__ == '__main__':
    MRGrepJob.run()
