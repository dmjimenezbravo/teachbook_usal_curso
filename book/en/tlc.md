# Central Limit Theorem

The **Central Limit Theorem** (CLT) is a fundamental result in probability theory and statistics. It states that, given certain conditions, the sample mean of a sufficiently large number of independent and identically distributed (i.i.d.) random variables will be approximately normally distributed, regardless of the underlying distribution of the original population.

## Mathematical Expression

Let $X_1, X_2, \dots, X_n$ be a sequence of i.i.d. random variables drawn from a population with expected value $\mu$ and finite variance $\sigma^2$. As the sample size $n$ increases, the distribution of the sample mean $\bar{X}_n$ approaches a normal distribution.

The standardization of the sum of these variables is expressed by the following equation:

$$
Z_n = \frac{\bar{X}_n - \mu}{\sigma / \sqrt{n}}
$$ (eq-clt)

As $n \to \infty$, the random variable $Z_n$ converges in distribution to the standard normal distribution $\mathcal{N}(0,1)$:

$$
\lim_{n \to \infty} P(Z_n \le z) = \Phi(z) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{z} e^{-t^2/2} dt
$$ (eq-normal-convergence)

```{admonition} Important Note
:class: important

The CLT is the reason why the normal distribution is so prevalent in nature and in statistical analysis. It allows making statistical inferences about population means even if the original distribution is not normal, provided the sample is sufficiently large (typically $n \ge 30$).
```
