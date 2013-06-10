import argparse
import json
import sys

import gnupg


def main(args=None):
    parser = argparse.ArgumentParser(description="""
        Encrypt each line of text with the given PGP private key.
    """)
    parser.add_argument('key_file', type=argparse.FileType('r'),
                        help='ASCII file containing PGP private key')
    parser.add_argument('input_files', type=argparse.FileType('r'),
                        default=[sys.stdin], nargs='*',
                        help='File(s) to encrypt. Default to stdin.')
    parser.add_argument('--password', help='Private key password, if any')
    parser.add_argument('-o', '--output', nargs='?', default=sys.stdout,
                        type=argparse.FileType('wb'),
                        help='Output file if not stdout')

    args = parser.parse_args(args)

    # make sure key is imported
    gpg = gnupg.GPG(gnupghome='~/.gnupg')
    key_data = args.key_file.read()
    import_result = gpg.import_keys(key_data)

    for f in args.input_files:
        for line in f:
            args.output.write(
                json.dumps({
                    'text': str(gpg.encrypt(
                        line.rstrip(), ['steve+bigdive@steveasleep.com'])),
                    'recipient': 'steve+bigdive@steveasleep.com'
                }))
            args.output.write('\n')


if __name__ == '__main__':
    main()
