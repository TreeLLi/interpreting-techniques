# LIME - Local Interpretable Model-Agnostic Explanations

we present the implementation of LIME there. To obtain the explanation of one single prediction, we: 

1. sample perturbed instances sorrunding the given input
2. weight each instance by its distance to the input, in order to assure the locality
3. optimise the explanation model to be faithful enough in approximating the original model while also to be interpretable as much as possible i.e. less complexity.

## Sampling

sample by drawing non-zero elements from the input.

1. transform the input in a form of binary vector in which each entry represent a super-pixel, i.e. an area potentially interpretable, and its value, 1 or 0, indicates the presence or absence of the associated area.
2. draw elements randomly from the super-pixel vectors and each draw constitutes a perturbed instance which may or may not be close to the given input

## Weighting

greater weight an instance is assigned, closer to the given input.

1. retrieve the sampled instances into the input space i.e. RGB vectors
2. compute the distance, in the original input space, to the original input for each instance
3. weight each with its distance

## Optimisation

parameterise a linear model to fit the weighted instances while keeping simple.

1. feedforward each retrieved instance into the original model and reserve the output as its label
2. optimise an explanation model towards the fidelity and interpretability:
   * minimise the weighted classification loss of the explanation model
   * minimise the complexity of the explanation model

