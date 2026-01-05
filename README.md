 Sistema de Predicción del Rendimiento Agrícola usando Árbol de Decisión y k-NN
🌾 Descripción general

Este proyecto implementa un sistema de aprendizaje supervisado capaz de predecir el rendimiento agrícola (Alto, Medio o Bajo) de un cultivo utilizando dos algoritmos fundamentales estudiados en el libro Artificial Intelligence: A Modern Approach (AIMA):

Árbol de Decisión (ID3) – Capítulo 18

k-Nearest Neighbors (k-NN) – Capítulo 20.4

El sistema está desarrollado en Python puro, sin librerías pesadas, para asegurar compatibilidad con computadoras de bajo rendimiento y ambientes educativos.

Se utiliza un dataset ampliado que contiene entre 40 y 60 registros, con variables reales del contexto agrícola. Esto permite obtener un aprendizaje más estable y resultados más representativos que en proyectos muy básicos.

🎯 Objetivo del proyecto

Desarrollar un modelo sencillo pero robusto de Inteligencia Artificial que:

Prediga el rendimiento agrícola basándose en características del cultivo.

Permita comparar el desempeño entre dos algoritmos clásicos de aprendizaje.

Sea eficiente en máquinas de bajo rendimiento.

Muestre paso a paso el funcionamiento interno de cada algoritmo.

Genere un análisis final del mejor método según el dataset utilizado.

📊 Características del dataset

El proyecto incluye un dataset en formato .csv o lista en Python, compuesto por aproximadamente 40–60 registros, cada uno con los siguientes atributos:

area_ha → Área sembrada (hectáreas)

agua_m3 → Volumen de agua utilizado

suelo → Tipo de suelo (Arenoso, Franco, Arcilloso)

cultivo → Tipo de cultivo (Maíz, Frijol, Arroz, Yuca, etc.)

riego → Técnica de riego (Goteo, Aspersión, Gravedad)

fertilizacion → Nivel de fertilización (Alta, Media, Baja)

rendimiento → Variable objetivo (Alto, Medio, Bajo)

El tamaño del dataset permite:

Árboles de decisión más profundos y explicativos

Mejor precisión en k-NN

Comparación realista entre modelos

🧠 Algoritmos implementados
1. 🌳 Árbol de Decisión (ID3)

Cálculo de entropía

Ganancia de información por atributo

Construcción recursiva del árbol

Predicción basada en las reglas aprendidas

Visualización del árbol en formato de texto

Este algoritmo es excelente para interpretación y análisis.

2. 👥 k-NN (k-Nearest Neighbors)

Implementado desde cero

Distancia Euclidiana

Conversión de atributos categóricos → valores numéricos simples

Predicción por votación mayoritaria

Pruebas con diferentes valores de k

k-NN es simple, directo y muy estable para datasets medianos.

🧪 Flujo general del sistema

Cargar el dataset

Entrenar el Árbol de Decisión

Guardar los registros para k-NN

Solicitar un caso nuevo al usuario

Predecir usando ambos algoritmos

Comparar resultados

Mostrar cuál modelo tuvo mejor precisión en pruebas internas

Presentar una conclusión final para el usuario

🔧 Requisitos

Solo necesitas:

Python 3.x

Sin librerías externas obligatorias

Funciona incluso en procesadores muy lentos con 2 GB de RAM

💻 Ejecución
python main.py


El sistema solicitará datos del cultivo y generará predicciones usando ambos métodos.

📈 Resultados esperados

El proyecto producirá:

Un árbol de decisión completo

Predicciones precisas de rendimiento

Comparación detallada entre Árbol de Decisión y k-NN

Un pequeño análisis estadístico del porcentaje de aciertos

Interpretación intuitiva para el usuario final

🧾 Justificación académica

Este proyecto se basa en fundamentos teóricos y prácticos de los capítulos:


Capítulo 18 – Aprendizaje de observaciones (Decision Tree Learning)

Capítulo 20.4 – Aprendizaje basado en instancias (k-NN)

del libro “Artificial Intelligence: A Modern Approach (AIMA)”, una de las referencias académicas más utilizadas en IA.

La comparación entre dos algoritmos clásicos refuerza la comprensión del aprendizaje supervisado y la toma de decisiones basada en datos.

🏁 Conclusión

Este proyecto demuestra cómo dos algoritmos relativamente simples pueden producir resultados útiles en problemas agrícolas reales, incluso con recursos computacionales limitados. La combinación de:

Dataset ampliado

Árbol de decisión interpretable

k-NN estable

Python puro
