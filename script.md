## Introduction

(SigmoidCurves Scene)

Hello everyone, in this video I will walkthrough the paper, Grokking Beyond Neural Networks, which I co-wrote with Charles O'Neill and Thang Bui.

Let's first define grokking. This is a phenomenon originally found in the accuracy curves of neural networks. It is characterised by a signficiant gap between the performance of the network on a training set, drawn in blue, when compared to a validation set, drawn in red. The difference in timing between these two curves is known as the grokking gap or delta k (animation pause).

(Summary of Paper Scene)

In our paper, we demonstrate three important properties of grokking:

1. Grokking occurs outside of neural networks (animation pause). In fact, it can be found in Gaussian process regression, Gaussian process classification and linear regression.
2. One can induce grokking via a particular data augmentation technique (animation pause). Specifically, if you append random bits to input examples, one sees a reliable increase in grokking.
3. There exists a coherent hypothesis which seems to explain grokking in cases where explicit regularisation is present and needed for grokking to occur.

## (1) Grokking outside of neural networks

(GP Training)

In all previous studies of grokking, the phenomenon has only been analysed in the context of neural network architectures. However, we have found that grokking can also occur in other contexts. Consider a Gaussian process classification task (animation pause). Suppose we wish for the GP to classify the parity of a given set of bits, let's say 3 (animation pause). However, we also add a set of additional random bits to the 3 relevant dimensions (animation pause). Given a set of labeled examples, we can then tune the hyperparameters of the GP via SGD. If one does so, one reliabely sees grokking accross different random initialisations.

## (2) Grokking via data augmentation

(concealment_strategy)

In the previous example, we were inherently using a data augmentation technique we call "concealment." In concealment, one considers example vectors used by a given model (animation pause). Then one adds to the original task a set of random bits. In the paper, we show that as one increases the number of these bits (animation pause), the grokking gap also increases (animation pause). Furthermore, for the range of values we tested, the trend appeared to be exponential.

## (3) Grokking and regularisation

(Loss function scene)

In most cases of grokking studied, the loss function (animation) used for optimisation includes a data fit term (animation pause) and a regularisation term (animation pause). Concurrently to the publication of our paper, it was shown that one could relax the need for the regularisation term in neural networks. However, we find for many of our settings, an explicit regularisation term is needed.

(Heatmap scene)

Take for example GP regression on a noisy sine wave. In this case, the negative marginal log likelihood (animation pause), the value we try to minimise, can be decomposed in two terms. The first term represents the data fit (animation pause) while the second term represents a complexity penalty (animation pause). (inlcude footnote about normalisation term). Let us examine the landscapes for these two terms with regard to the kernel hyperparameters (animation pause). Note that the x axis on each heatamp is the log output scale and the y axis is the lengthscale. A darker shde of red is indicative of a better model according to the criterion of the heatmap. As we can see, the data fit landscape has a basin of attraction for large output scale but for relatively small lengthscale. Alternatively, the complexity is large for small lengthscales and large outputscales. Let's track how three different initialisations evolve in the landscape (animation pause). It is trajectory B, initialised in a region of low-error high-complexity which exhibits grokking.

## A possible mechanism of grokking

(Heatmap scene continues...)

This observations leads us to hypothesise a possible mechansim for grokking. One will get grokking if low error high complexity solutions are relatively accessible but low error low complexity solutions are not. Due to the principle of parsimony, high complexity solutions should generalise poorly but low complexity solutions should generalise better. Thus, as the model transitions from low error high complexity solutions to low error low complexity solutions, we see a fairly sudden increase in generalisation performance. I.e. grokking.

## Conclusion

(Conclusion)

In conclusion, we hope our study has expanded somewhat our understanding of the grokking phenomenon. In future, we believe it would be fruitful to further investigate in what settings explicit regularisation is and is not required for grokking. In addition, it would be quite interesting to see a thoeretical justification for the concealment technique. Perhaps it has somethign to do with the volume of solutions in high dimensional spaces.

Thanks for watching and be sure to check out our paper, Grokking Beyond Neural Networks: An Empirical Exploration with Model Complexity, published in Transactions on Machine Learning Research. You can find the link in the description of this video.

I'd also like to thank Grant Sanderson of 3blue1brown fame for publishing Manim, the library used to animate this video and Vincent Rubinetti for providing the music. As you can probably tell, I was heavily inspired by their aesthetic.
