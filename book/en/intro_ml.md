# Introduction to Machine Learning

**Machine Learning** (ML) is a fundamental branch of Artificial Intelligence that allows computers to learn from data without being explicitly programmed. In this chapter, we will explore its origins, its current state, and the different subfields that make it up, using classic literature in the field as reference {cite:p}`james2013islr, chollet2021deep, geron2019hands`.

## Origin and Evolution

Historically, traditional programming required humans to write explicit rules (algorithms) that, when applied to data, produced answers. **Machine Learning** reverses this paradigm: the system receives data and the correct answers, and it takes charge of inferring the rules itself {cite:p}`chollet2021deep`.

```{admonition} Paradigm Shift
:class: tip
**Classical Programming:** Data + Rules $\rightarrow$ Answers  
**Machine Learning:** Data + Answers $\rightarrow$ Rules
```

Although the first learning algorithms date back to the mid-20th century, the field was dominated for a long time by symbolic artificial intelligence (based on static logical rules). It was starting in the 1990s that statistical learning gained momentum, consolidating itself thanks to the increase in computing power and data availability.

## Current State

Today, Machine Learning is behind most modern technological revolutions: from recommendation engines and computer vision, to large language models (LLMs).

**Deep Learning**, a subfield of ML that uses multilayer artificial neural networks, has been the main driver of this explosion {cite:p}`chollet2021deep`. Its success is mainly due to three concurrent factors:
1. **Hardware:** The massive use of GPUs (Graphics Processing Units) that allow parallelizing matrix operations.
2. **Big Data:** The immense amount of data generated on the internet.
3. **Algorithms:** Improvements in optimization and neural network architectures (such as Transformers).

## Machine Learning Subfields

Machine Learning is generally classified according to the type and amount of supervision the model receives during its training {cite:p}`geron2019hands`.

```{admonition} Main Classification
:class: note
1. **Supervised Learning**
2. **Unsupervised Learning**
3. **Reinforcement Learning**
```

### 1. Supervised Learning
The training dataset includes the desired solutions, called **labels**.
- **Classification:** The goal is to predict a discrete category (e.g., a spam filter).
- **Regression:** The goal is to predict a continuous numerical value (e.g., the price of a house).

### 2. Unsupervised Learning
The training data is unlabeled. The system tries to learn without a "teacher".
- **Clustering:** Grouping similar customers.
- **Dimensionality reduction:** Simplifying data without losing too much information.
- **Anomaly detection:** Identifying fraudulent bank transactions.

### 3. Reinforcement Learning
It is a very different approach. The learning system, called an **agent**, observes the environment, performs actions, and receives **rewards** (or penalties). It must learn by itself the best strategy (policy) to obtain the maximum reward over time. It is widely used in robotics and in artificial intelligences for games (e.g., AlphaGo).

````{only} html
## Bibliography for this page

```{bibliography}
:filter: docname in docnames
```
````
