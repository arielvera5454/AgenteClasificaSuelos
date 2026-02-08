import random
from dataset import DatasetLoader, CLASE_INV
from knn import KNNClassifier
from decision_tree import DecisionTreeClassifier
from validator import InputValidator

def k_fold_validation(X, y, modelo_tipo="knn", k_folds=5, k_neighbors=3):
    """Realiza validación cruzada manual sin librerías."""
    indices = list(range(len(X)))
    random.shuffle(indices)
    tamano_fold = len(X) // k_folds
    scores = []

    for i in range(k_folds):
        # Crear particiones
        test_idx = indices[i * tamano_fold : (i + 1) * tamano_fold]
        train_idx = [idx for idx in indices if idx not in test_idx]

        X_train = [X[j] for j in train_idx]
        y_train = [y[j] for j in train_idx]
        X_test = [X[j] for j in test_idx]
        y_test = [y[j] for j in test_idx]

        # Entrenar y evaluar
        aciertos = 0
        if modelo_tipo == "knn":
            model = KNNClassifier(k=k_neighbors)
            # KNN es lazy, no entrena, solo almacena
            predicciones = [model.predict(X_train, y_train, x) for x in X_test]
        else:
            model = DecisionTreeClassifier()
            model.fit(X_train, y_train)
            predicciones = [model.predict(x) for x in X_test]

        for real, pred in zip(y_test, predicciones):
            if real == pred: aciertos += 1
        
        scores.append(aciertos / len(y_test))

    return sum(scores) / len(scores)

def main():
    print("="*60)
    print("  AGENTE CLASIFICADOR DE SUELOS (Validado y Robusto)")
    print("="*60)

    loader = DatasetLoader()
    X_raw, y = loader.load_raw() # Carga datos limpios (sin leakage)

    # Preparar vistas de datos
    X_knn = loader.get_knn_data(X_raw)   # Normalizados 0-1
    X_tree = loader.get_tree_data(X_raw) # Discretizados (Rangos)

    print(f"✅ Datos cargados: {len(X_raw)} muestras.")
    print("🚫 Variables eliminadas: Plot, Field, Block (Evita Fuga de Información)")
    print("⚙️  Validación: 5-Fold Cross Validation (Evaluación Estadística Fuerte)\n")

    # Entrenar modelos finales con TODOS los datos para predicción
    final_knn = KNNClassifier(k=3)
    final_tree = DecisionTreeClassifier()
    final_tree.fit(X_tree, y) # Entrena con discretizados

    while True:
        print("\n1. Ver Validación Estadística (K-Fold) | 2. Predecir | 0. Salir")
        opcion = input("Opción: ")

        if opcion == "1":
            print("\nEvaluando K-NN (Normalizado)...")
            acc_knn = k_fold_validation(X_knn, y, "knn")
            print(f"📊 Precisión Promedio k-NN: {acc_knn:.2%}")

            print("Evaluando Árbol ID3 (Discretizado)...")
            acc_tree = k_fold_validation(X_tree, y, "tree")
            print(f"📊 Precisión Promedio Árbol: {acc_tree:.2%}")

        elif opcion == "2":
            val = InputValidator()
            try:
                # Solo pedimos datos FÍSICOS
                raw_input = [
                    val.validate_wheel(input("Tráfico (Trafficked/Untrafficked): ")),
                    val.validate_crop(input("Cultivo (AlfaCorn/CC): ")),
                    val.validate_tillage(input("Labranza (NT/CP): ")),
                    val.validate_side(input("Lado (E/W): ")),
                    val.validate_depth(input("Prof. Sup (cm): ")),
                    val.validate_depth(input("Prof. Inf (cm): ")),
                    val.validate_residue(input("Residuos (0-100): "))
                ]
                
                # Transformar input para cada modelo
                input_knn = loader.get_knn_data([raw_input])[0]
                input_tree = loader.get_tree_data([raw_input])[0]

                # Predecir
                # Pasamos X_knn y y completos para que busque vecinos
                r_knn = final_knn.predict(X_knn, y, input_knn) 
                r_tree = final_tree.predict(input_tree)

                print(f"\n🔍 k-NN: {CLASE_INV[r_knn]}")
                print(f"🌳 Árbol: {CLASE_INV[r_tree]}")

            except ValueError as e:
                print(f"❌ Error: {e}")

        elif opcion == "0":
            break

if __name__ == "__main__":
    main()