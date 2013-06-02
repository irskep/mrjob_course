"""
Write a function ``compute_common_friends`` that takes a list of file paths as
arguments and returns a nested dictionary of {'person 1': {'person 2': <number
of friends in common>}}.

Each line of input will have the format <name>\t<list of friends>, where both
values are JSON-encoded. For example, this could be ``input.txt``:

    "Steve Johnson"\t["Tim Henderson", "Fred Hatfull", "Toby Waite"]
    "Fred Hatfull"\t["Steve Johnson", "Toby Waite"]
    "Toby Waite"\t["Steve Johnson", "Fred Hatfull"]
    "Tim Henderson"\t["Steve Johnson"]

The function would be called like this:

    compute_common_friends(['input.txt'])

It should return this output:

    {
        'Steve Johnson': {
            'Fred Hatfull': 1,
            'Tim Henderson': 0,
            'Toby Waite': 1,
        },
        'Fred Hatfull': {
            'Steve Johnson': 1,
            'Toby Waite': 1,
        },
        'Toby Waite': {
            'Steve Johnson': 1,
            'Fred Hatfull': 1,
        },
        'Tim Henderson': {
            'Steve Johnson': 0,
        },
    }
"""

from mrjob.job import MRJob


class MRCommonFriendsJob(MRJob):
    pass


if __name__ == '__main__':
    MRCommonFriendsJob.run()
