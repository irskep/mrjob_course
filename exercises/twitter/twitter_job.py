from mrjob.job import MRJob
from mrjob.protocol import JSONValueProtocol


class TwitterJob(MRJob):

    INPUT_PROTOCOL = JSONValueProtocol
    OUTPUT_PROTOCOL = JSONValueProtocol

    def steps(self):
        return [self.mr(mapper=self.filter_geo)]

    def filter_geo(self, _, tweet):
        if tweet['geo']:
            yield None, tweet['geo']


if __name__ == '__main__':
    TwitterJob().run()
