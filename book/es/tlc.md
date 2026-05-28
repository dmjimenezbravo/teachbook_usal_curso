# Teorema del Límite Central

El **Teorema del Límite Central** (TLC) es un resultado fundamental en la teoría de la probabilidad y estadística. Establece que, dadas ciertas condiciones, la media muestral de una cantidad suficientemente grande de variables aleatorias independientes e idénticamente distribuidas (i.i.d.) tendrá una distribución aproximadamente normal, independientemente de la distribución subyacente de la población original.

## Expresión Matemática

Sea $X_1, X_2, \dots, X_n$ una secuencia de variables aleatorias i.i.d. extraídas de una población con valor esperado $\mu$ y varianza finita $\sigma^2$. A medida que el tamaño de la muestra $n$ aumenta, la distribución de la media muestral $\bar{X}_n$ se aproxima a una distribución normal.

La estandarización de la suma de estas variables se expresa mediante la siguiente ecuación:

$$
Z_n = \frac{\bar{X}_n - \mu}{\sigma / \sqrt{n}}
$$ (eq-tlc)

A medida que $n \to \infty$, la variable aleatoria $Z_n$ converge en distribución a la distribución normal estándar $\mathcal{N}(0,1)$:

$$
\lim_{n \to \infty} P(Z_n \le z) = \Phi(z) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{z} e^{-t^2/2} dt
$$ (eq-convergencia-normal)

```{admonition} Nota Importante
:class: important

El TLC es la razón por la cual la distribución normal es tan prevalente en la naturaleza y en el análisis estadístico. Permite realizar inferencias estadísticas sobre medias poblacionales incluso si la distribución original no es normal, siempre que la muestra sea lo suficientemente grande (típicamente $n \ge 30$).
```
