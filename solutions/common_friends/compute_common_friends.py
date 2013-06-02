from common_friends_job import MRCommonFriendsJob


def compute_common_friends(input_paths):
    mr_job = MRCommonFriendsJob(
        ['--runner=inline', '--strict-protocols'] + input_paths)
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
