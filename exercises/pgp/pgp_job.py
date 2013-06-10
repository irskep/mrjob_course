"""
"""
import gnupg

from mrjob.job import MRJob
from mrjob.launch import _READ_ARGS_FROM_SYS_ARGV
from mrjob.protocol import (
    JSONValueProtocol,
    RawValueProtocol,
)


always_args = [
    '--bootstrap-cmd',
    'sudo apt-get install gnupg',
    '--bootstrap-cmd',
    'sudo python -m easy_install python-gnupg',
]


class MRPGPJob(MRJob):

    INPUT_PROTOCOL = JSONValueProtocol
    OUTPUT_PROTOCOL = RawValueProtocol

    def load_options(self, args):
        args += always_args
        super(MRPGPJob, self).load_options(args)

    def mapper_init(self):
        self.gpg = gnupg.GPG(gnupghome='~/.gnupg')
        with open('D0736C1B_priv.asc', 'r') as f:
            self.import_result = self.gpg.import_keys(f.read())
            yield None, self.import_result.results

    def mapper(self, _, line):
        yield None, self.gpg.decrypt(line['text'], passphrase='mrjob')


if __name__ == '__main__':
    MRPGPJob.run()
