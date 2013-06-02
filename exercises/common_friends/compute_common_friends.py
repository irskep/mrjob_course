from common_friends_job import MRCommonFriendsJob


def compute_common_friends(input_paths):
    mr_job = MRCommonFriendsJob(
        ['--runner=inline', '--strict-protocols'] + input_paths)

    result = {}

    with mr_job.make_runner() as runner:
        runner.run()
        for line in runner.stream_output():
            a, b = mr_job.parse_output_line(line)

    return result
