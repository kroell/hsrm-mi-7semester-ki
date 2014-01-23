#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''

Perceptron Implementation. 

Definition:
Input (x) can be R, w can be R, output (y) can be between -1 or 1

Learning comes through a iterative optimizing:
1. Take random Weights (w)
2. Iterate how often you want
3. Every Iteration:
	3.1 Classify a training example (xi) and equal y with the result of Φ(xi)
	3.2 if Φ(xi) != y, then correct weights so that Φ(xi) is comming closer to y



MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated 
documentation files (the "Software"), to deal in the Software without restriction, including without limitation 
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, 
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions 
of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED 
TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL 
THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF 
CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER 
DEALINGS IN THE SOFTWARE.
'''


from random import choice 
from numpy import array, dot, random
from pylab import plot, ylim, savefig


'''
training_data = array(input value, input value, bias to move treshold), expected result
'''
# OR 
training_data_or = [ 
	(array([0,0,1]), 0),
	(array([0,1,1]), 1),
	(array([1,0,1]), 1), 
	(array([1,1,1]), 1), 
]
# AND 
training_data_and = [ 
	(array([0,0,1]), 0),
	(array([0,1,1]), 0),
	(array([1,0,1]), 0), 
	(array([1,1,1]), 1), 
]

# NOT
training_data_not = [ 
	(array([0,0,1]), 0),
	(array([0,1,1]), 1),
	(array([1,0,1]), 1), 
	(array([1,1,1]), 1), 
]

# NOR
training_data_nor = [ 
	(array([0,0,1]), 1),
	(array([0,1,1]), 0),
	(array([1,0,1]), 0), 
	(array([1,1,1]), 0), 
]

# initial weights 
w = random.rand(3)


errors = [] # stores error values for plotting
learning_rate = 0.15 # learning_rate normally < 0.1
number_of_learning_iterations = 150


# activation function to calc Φ(x), slide 15
def activation_function(x):
	return 0 if x < 0 else 1


if __name__ == '__main__':

	# learning through iterative optimazing, slide 25
	for i in xrange(number_of_learning_iterations): 
		x, expected = choice(training_data_and) # random input set from the training data
		scalar_product = dot(w, x) # calc scalar product
		error = expected - activation_function(scalar_product)
		errors.append(error) # for plotting
		w += learning_rate * error * x # correct weight so that Φ(x) nears expected

	# print it
	for x, _ in training_data_and: 
		scalar_product = dot(x, w) 
		print("{}: {} -> {}".format(x[:2], scalar_product, activation_function(scalar_product)))

	# plot it
	ylim([-1,1]) 
	plot(errors)
	savefig('AND.png')



	