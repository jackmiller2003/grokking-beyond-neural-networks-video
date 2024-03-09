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

In most cases of grokking studied, the loss function (animation) used for optimisation included a data fit term (animation pause) and a regularisation term (animation pause). Concurrently to the publication of our paper, it was shown that one could relax the need for the regularisation term in neural networks.
