"""
business name: [{checkin}, {checkin}]
"""
from mrjob.job import MRJob
from mrjob.protocol import JSONValueProtocol


class JoinJob(MRJob):

    INPUT_PROTOCOL = JSONValueProtocol

    def steps(self):
        return [self.mr(mapper=self.map_input,
                        reducer=self.join_checkins_to_business)]

    def map_input(self, _, item):
        if item['type'] == 'checkin':
            yield item['business_id'], item
        elif item['type'] == 'business':
            yield item['business_id'], item

    def join_checkins_to_business(self, business_id, items):
        everything = list(items)
        try:
            business = [i for i in everything if i['type'] == 'business'][0]
            checkins = [i for i in everything if i['type'] == 'checkin']
            business['checkins'] = checkins
            yield business['name'], business
        except IndexError:  # no business object, woooooooo!
            pass


if __name__ == '__main__':
    JoinJob().run()
