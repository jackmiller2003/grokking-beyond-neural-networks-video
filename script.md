## Introduction

Grokking is a phenomenon originally found in the accuracy curves of neural networks. It is characterised by a signficiant gap between the performance of the network on a training set (animation pause) when compared to a validation set (animation pause). The difference in timing between these two curves is known as the grokking gap (animation pause).

In our paper, Grokking Beyond Neural Networks, we demonstrate three important properties of the phenomenon:

1. Grokking occurs outside of neural networks (animation pause). It can be found in Gaussian process regression, Gaussian process classification and linear regression.
2. One can induce grokking via a particular data augmentation technique (animation pause). Specifically, if you append random bits to input examples, one sees a reliable increase in grokking.
3. Explicit regularisation is required for grokking to occur in certain settings (animation pause).

One can read more about these points in the paper linked in the description of this video.

## (1) Grokking outside of neural networks

In all previous studies of grokking, the phenomenon has only been analysed in the context of neural network architectures. However, we have found that grokking can also occur in other contexts. For example, take the case of Gaussian process classification (animation pause). Suppose we wish to predict the parity of a given set of bits, let's say 3 (animation pause). Imagine we also add a set of additional random bits to the 3 relevant dimensions (animation pause). Suppose then we tune the hyperparameters of a Gaussian process via stochastic gradient descent. Surprisingly, this setting induces grokking.

## (2) Grokking via data augmentation

In the previous exampel, we were inherently using a data augmentation technique we call "concealment." In concealment, one considers example vectors used by a given model (animation pause). Then one adds to the original task a set of random bits. We show that as one increases the number of these bits (animation pause), the grokking gap also increases (animation pause). Furthermore, for the range of values we tested, the trend appeared to be exponential.

## (3) Grokking and regularisation

In most cases of grokking studied, the loss function (animation) used for optimisation includes a data fit term (animation pause) and a regularisation term (animation pause). Concurrently to the publication of our paper, it was shown that one could relax the need for the regularisation term in neural networks. However, we find for many of our settings, an explicit regularisation term is needed.

Take for example GP regression on a noisy sine wave. In this case, the negative marginal log likelihood (animation pause), the value we try to minimise, can be decomposed in two terms. The first term represents the data fit (animation pause) while the second term represents a complexity penalty (animation pause). (inlcude footnote about normalisation term). Let us examine the landscapes for these two terms with regard to the kernel hyperparameters (animation pause). As we can see, the data fit landscape has a basin of attraction for large output scale but for relatively small lengthscale. Alternatively, the complexity is large for small lengthscales and large outputscales. Let's track how three different initialisations evolve in the landscape (animation pause). As we can see, it is initialisation B, which started in a region of low-error high-complexity which exhibited grokking.

## A possible mechanism of grokking

This observations leads us to hypothesise a possible mechansim for grokking. One will get grokking if low error high complexity solutions are relatively accessible but low error low complexity solutions are not. Due to the principle of parsimony, high complexity solutions should generalise poorly but low complexity solutions should generalise better. Thus, as the network transitions from low error high complexity solutions to low error low complexity solutions, we see a fairly sudden increase in generalisation performance. I.e. grokking.

## Conclusion

In conclusion, we hope our study has expanded somewhat our understanding of the grokking phenomenon. In future, we believe it would be fruitful to further investigate in what settings explicit regularisation is required when compared to those settings where it is not. In addition, a thoeretical justification for the concealment technique might be derived from our proposed mechanism.
