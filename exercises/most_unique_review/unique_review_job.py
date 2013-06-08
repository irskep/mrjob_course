from mrjob.job import MRJob


class MRUniqueReviewJob(MRJob):

    def steps(self):
        return [self.mr(mapper=self.mapper_friend_list_pairs,
                        reducer=self.reducer_friend_list_intersection_size)]

    def mapper_friend_list_pairs(self, name, friends):
        for friend in friends:
            yield sorted([name, friend]), friends

    def reducer_friend_list_intersection_size(self, friend_pair, friend_lists):
        friend_lists = list(friend_lists)
        if len(friend_lists) > 1:
            num = len(set(friend_lists[0]) & set(friend_lists[1]))
            yield friend_pair, num
        else:
            yield friend_pair, {}


if __name__ == '__main__':
    MRUniqueReviewJob.run()
