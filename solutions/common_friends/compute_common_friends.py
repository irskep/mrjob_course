import logging
import sys

from common_friends_job import MRCommonFriendsJob


logging.basicConfig()


def compute_common_friends(input_paths):
    mr_job = MRCommonFriendsJob(
        ['--runner=local', '--strict-protocols'] + input_paths)
    logging.getLogger('mrjob').setLevel(logging.INFO)

    result = {}

    with mr_job.make_runner() as runner:
        runner.run()
        for line in runner.stream_output():
            friend_pair, num = mr_job.parse_output_line(line)
            result.setdefault(friend_pair[0], {})
            result.setdefault(friend_pair[1], {})
            result[friend_pair[0]][friend_pair[1]] = num
            result[friend_pair[1]][friend_pair[0]] = num

    return result


if __name__ == '__main__':
    for name, friends in compute_common_friends(sys.argv[1:]).viewitems():
        for name2, friends2 in friends.viewitems():
            if friends2:
                print '%r %r %r' % (name, name2, friends2)
