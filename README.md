# Clasificador de Compactación del Suelo 🌱

Proyecto académico de **aprendizaje supervisado** para la clasificación del nivel de compactación del suelo agrícola, desarrollado **sin librerías externas de machine learning**, como parte de un trabajo universitario.

---

## 📌 Descripción general

La compactación del suelo afecta negativamente el crecimiento de los cultivos y la productividad agrícola. Este proyecto implementa un **sistema clasificador** capaz de predecir el nivel de compactación del suelo (**baja, media o alta**) a partir de variables de manejo y profundidad, utilizando datos reales de campo.

El sistema fue desarrollado desde cero, implementando manualmente los algoritmos:

- **k-Nearest Neighbors (k-NN)**
- **Árbol de Decisión ID3**

con el objetivo de reforzar los fundamentos teóricos del aprendizaje automático.

---

## 🎯 Objetivos del proyecto

- Aplicar técnicas de **aprendizaje supervisado clásico**.
- Implementar algoritmos de clasificación **sin usar librerías externas**.
- Clasificar el nivel de compactación del suelo usando el **Cone Index**.
- Evaluar los modelos mediante **validación cruzada k-Fold**.
- Garantizar un enfoque metodológicamente correcto y defendible académicamente.

---

## 📊 Conjunto de datos

El dataset contiene mediciones realizadas en parcelas agrícolas, incluyendo información sobre:

- Tráfico del suelo (`Wheel`)
- Profundidad de medición (`Depth.Upper`, `Depth.Lower`)
- Tipo de cultivo (`Crop`)
- Sistema de labranza (`Tillage`)
- Residuos de cosecha (`ResidueRemoved`)
- Índice de penetración (`ConeIndex`)

### Variable objetivo

El **Cone Index** (MPa) se discretiza en tres clases:

| Clase | Rango (MPa) | Nivel de compactación |
|------|------------|-----------------------|
| 0 | < 1.0 | Baja |
| 1 | 1.0 – 2.0 | Media |
| 2 | > 2.0 | Alta |

---

## ⚙️ Preprocesamiento

- Eliminación de identificadores espaciales para evitar *data leakage*.
- Normalización Min-Max para k-NN.
- Discretización de variables continuas para el Árbol ID3.
- Manejo de valores faltantes.

---

## 🤖 Modelos implementados

### k-Nearest Neighbors (k-NN)

- Distancia euclidiana
- k = 3
- Aprendizaje basado en instancias

### Árbol de Decisión ID3

- Basado en entropía y ganancia de información
- Variables categóricas
- Reglas interpretables

---

## 📈 Evaluación

Se utilizó **validación cruzada k-Fold (k=5)** implementada manualmente.

### Métrica principal

- **Accuracy (Exactitud)**

```text
Accuracy = predicciones correctas / total de predicciones
```

---

## ▶️ Ejecución del proyecto

Desde la carpeta raíz del proyecto:

```bash
python src/main.py
```

El script realiza automáticamente:

1. Carga del dataset
2. Preprocesamiento
3. Entrenamiento de los modelos
4. Evaluación con validación cruzada
5. Impresión de resultados en consola

---

## 📚 Requisitos

- Python 3.8 o superior
- No se utilizan librerías externas de machine learning
- Solo librerías estándar de Python

---

## 🎓 Contexto académico

Este proyecto fue desarrollado con **fines educativos**, como parte de un curso universitario relacionado con:

- Inteligencia Artificial
- Aprendizaje Automático
- Ciencia de Datos
- Informática / Ingeniería

Todas las decisiones de diseño están justificadas metodológicamente en el informe del proyecto.

---

## 🚀 Trabajo futuro

- Inclusión de variables físico-químicas del suelo (BD, GWC, VWC)
- Implementación de nuevos clasificadores
- Análisis con métricas adicionales (Precision, Recall, F1)
- Visualización de resultados

---

## 👤 Autor

**Ariel Vera**  
Proyecto universitario – 2026

---

## 📄 Licencia

Este proyecto se distribuye únicamente con fines académicos y educativos.

