
import random


class Evaluator:
    def __init__(self, p=0.7):
        self.p = p

    def split(self, X, y):
        idx = list(range(len(X)))
        random.shuffle(idx)
        c = int(len(X) * self.p)

        return (
            [X[i] for i in idx[:c]],
            [X[i] for i in idx[c:]],
            [y[i] for i in idx[:c]],
            [y[i] for i in idx[c:]],
        )

    def accuracy(self, y_real, y_pred):
        aciertos = 0
        for i in range(len(y_real)):
            if y_real[i] == y_pred[i]:
                aciertos += 1
        return aciertos / len(y_real)

