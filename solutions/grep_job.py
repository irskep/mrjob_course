"""
Filter input lines by POSIX regular expression. The expression to use should be
supplied by the command line argument -e or --expression. It should use POSIX
extended regular expressions if --extended is passed.

The difference is described here:
    http://www.regular-expressions.info/posix.html#bre

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

from optparse import OptionError

from mrjob.job import MRJob
from mrjob.protocol import RawValueProtocol
from mrjob.util import cmd_line


class MRGrepJob(MRJob):

    INPUT_PROTOCOL = RawValueProtocol  # this is the default
    OUTPUT_PROTOCOL = RawValueProtocol

    def configure_options(self):
        super(MRGrepJob, self).configure_options()
        self.add_passthrough_option('-e', '--expression')
        self.add_passthrough_option('--extended', action='store_true')

    def load_options(self, *args, **kwargs):
        super(MRGrepJob, self).load_options(*args, **kwargs)
        if not self.options.expression:
            raise OptionError("The -e flag is required.")

    def mapper_cmd(self):
        cmd = ['grep']
        if self.options.extended:
            cmd.append('-e')
        cmd.append(self.options.expression)
        return ' '.join(cmd)


if __name__ == '__main__':
    MRGrepJob.run()
