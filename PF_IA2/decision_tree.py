
import math


class DecisionTreeClassifier:
    """Simple ID3 decision tree classifier implementation."""
    def __init__(self):
        self.tree = None
        self.default = None

    @staticmethod
    def _entropia(y):
        total = len(y)
        conteo = {}
        for e in y:
            conteo[e] = conteo.get(e, 0) + 1
        return -sum((c / total) * math.log2(c / total) for c in conteo.values())

    def _ganancia(self, X, y, atributo):
        ent_ini = self._entropia(y)
        subsets = {}
        for i in range(len(X)):
            subsets.setdefault(X[i][atributo], []).append(y[i])

        ent_cond = sum((len(s) / len(y)) * self._entropia(s) for s in subsets.values())
        return ent_ini - ent_cond

    @staticmethod
    def _clase_mayoritaria(y):
        return max(set(y), key=y.count)

    def _construir(self, X, y, atributos):
        if len(set(y)) == 1:
            return y[0]

        if not atributos:
            return self._clase_mayoritaria(y)

        mejor = max(atributos, key=lambda a: self._ganancia(X, y, a))
        arbol = {"atributo": mejor, "ramas": {}}

        valores = set(x[mejor] for x in X)

        for v in valores:
            X_sub, y_sub = [], []
            for i in range(len(X)):
                if X[i][mejor] == v:
                    X_sub.append(X[i])
                    y_sub.append(y[i])

            nuevos_atributos = atributos.copy()
            nuevos_atributos.remove(mejor)

            arbol["ramas"][v] = (
                self._construir(X_sub, y_sub, nuevos_atributos)
                if X_sub else self._clase_mayoritaria(y)
            )

        return arbol

    def _predecir(self, arbol, x):
        if not isinstance(arbol, dict):
            return arbol

        valor = x[arbol["atributo"]]
        if valor not in arbol["ramas"]:
            return self.default
        return self._predecir(arbol["ramas"][valor], x)

    def fit(self, X, y):
        atributos = list(range(len(X[0]))) if X else []
        self.tree = self._construir(X, y, atributos)
        self.default = self._clase_mayoritaria(y)

    def predict(self, x):
        return self._predecir(self.tree, x)

