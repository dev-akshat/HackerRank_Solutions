from functools import cmp_to_key


class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        pass

    def comparator(a, b):
        if a.score > b.score:
            return -1
        elif a.score < b.score:
            return 1
        else:
            if a.name > b.name:
                return 1
            else:
                return -1


data1 = "amy 100, david 100, heraldo 50, aakansha 75, aleksa 150".split(sep=", ")
data2 = []
for x in data1:
    name, score = x.split()
    data2.append(Player(name, int(score)))
data2 = sorted(data2, key=cmp_to_key(Player.comparator))
for i in data2:
    print(i.name, i.score)
