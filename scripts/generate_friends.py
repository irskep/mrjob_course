import json

from collections import defaultdict
from random import (
    choice,
    randint
)

names = []

with open('data/names.txt') as f:
    for line in f:
        names.append(line.strip())

friends = defaultdict(set)

for name in names:
    num_friends = randint(1, 100)
    while len(friends[name]) < num_friends:
        friends[name].add(choice(names))

with open('data/friends.txt', 'w') as f:
    for name, friend_names in friends.viewitems():
        f.write('%s\t%s\n' % (
            json.dumps(name), json.dumps(list(friend_names))))
