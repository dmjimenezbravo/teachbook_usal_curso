# Introducción al Machine Learning

El **Machine Learning** (Aprendizaje Automático) es una rama fundamental de la Inteligencia Artificial que permite a las computadoras aprender de los datos sin ser explícitamente programadas. En este capítulo, exploraremos su origen, su estado actual y los diferentes subcampos que lo componen, utilizando como referencia literatura clásica del área {cite:p}`james2013islr, chollet2021deep, geron2019hands`.

## Origen y Evolución

Históricamente, la programación tradicional requería que los humanos escribieran reglas explícitas (algoritmos) que, aplicadas a los datos, produjeran respuestas. El **Machine Learning** invierte este paradigma: el sistema recibe datos y las respuestas correctas, y él mismo se encarga de inferir las reglas {cite:p}`chollet2021deep`.

```{admonition} Cambio de Paradigma
:class: tip
**Programación Clásica:** Datos + Reglas $\rightarrow$ Respuestas  
**Machine Learning:** Datos + Respuestas $\rightarrow$ Reglas
```

Aunque los primeros algoritmos de aprendizaje datan de mediados del siglo XX, durante mucho tiempo el campo estuvo dominado por la inteligencia artificial simbólica (basada en reglas lógicas estáticas). Fue a partir de los años 90 cuando el aprendizaje estadístico cobró fuerza, consolidándose gracias al aumento de la capacidad de cómputo y la disponibilidad de datos.

## Estado Actual

Hoy en día, el Machine Learning está detrás de la mayoría de las revoluciones tecnológicas modernas: desde los motores de recomendación y la visión por computadora, hasta los grandes modelos de lenguaje (LLMs).

El **Deep Learning** (Aprendizaje Profundo), un subcampo del ML que utiliza redes neuronales artificiales multicapa, ha sido el principal motor de esta explosión {cite:p}`chollet2021deep`. Su éxito se debe principalmente a tres factores concurrentes:
1. **Hardware:** El uso masivo de GPUs (Unidades de Procesamiento Gráfico) que permiten paralelizar operaciones matriciales.
2. **Big Data:** La inmensa cantidad de datos generados en internet.
3. **Algoritmos:** Mejoras en la optimización y en las arquitecturas de redes neuronales (como los Transformers).

## Subcampos del Machine Learning

El Machine Learning se clasifica generalmente según el tipo y cantidad de supervisión que el modelo recibe durante su entrenamiento {cite:p}`geron2019hands`.

```{admonition} Clasificación Principal
:class: note
1. **Aprendizaje Supervisado (Supervised Learning)**
2. **Aprendizaje No Supervisado (Unsupervised Learning)**
3. **Aprendizaje por Refuerzo (Reinforcement Learning)**
```

### 1. Aprendizaje Supervisado
El conjunto de datos de entrenamiento incluye las soluciones deseadas, llamadas **etiquetas** (labels). 
- **Clasificación:** El objetivo es predecir una categoría discreta (ej. filtro de spam).
- **Regresión:** El objetivo es predecir un valor numérico continuo (ej. precio de una vivienda).

### 2. Aprendizaje No Supervisado
Los datos de entrenamiento no están etiquetados. El sistema intenta aprender sin un "profesor".
- **Clustering (Agrupamiento):** Agrupar clientes similares.
- **Reducción de dimensionalidad:** Simplificar los datos sin perder demasiada información.
- **Detección de anomalías:** Identificar transacciones bancarias fraudulentas.

### 3. Aprendizaje por Refuerzo
Es un enfoque muy diferente. El sistema de aprendizaje, llamado **agente**, observa el entorno, realiza acciones y recibe **recompensas** (o penalizaciones). Debe aprender por sí mismo la mejor estrategia (política) para obtener la máxima recompensa a lo largo del tiempo. Es ampliamente utilizado en robótica y en inteligencias artificiales para juegos (ej. AlphaGo).

````{only} html
## Bibliografía de esta página

```{bibliography}
:filter: docname in docnames
```
````
