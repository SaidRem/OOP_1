def vote(votes):
    u_votes = set(votes)
    d = dict()
    for n in u_votes:
        encounters = sum(1 for i in votes if i == n)
        d.setdefault(n, encounters)
    return max(d, key=d.get)


if __name__ == '__main__':
    print(vote([1, 1, 1, 2, 3]))
    print(vote([1, 2, 3, 2, 2]))
