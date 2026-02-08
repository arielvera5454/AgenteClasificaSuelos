import math


class KNNClassifier:
    def __init__(self, k=3):
        self.k = k

    def _dist(self, a, b):
        return math.sqrt(sum((a[i] - b[i]) ** 2 for i in range(len(a))))

    def predict(self, X, y, x):
        dists = [(self._dist(X[i], x), y[i]) for i in range(len(X))]
        dists.sort(key=lambda z: z[0])

        votes = {}
        for _, label in dists[:self.k]:
            votes[label] = votes.get(label, 0) + 1

        return max(votes, key=votes.get)
