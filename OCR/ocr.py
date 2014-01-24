#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
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


# activation function to calc Φ(x), slide 15
def activation_function(x):
	return 0 if x < 0 else 1



def main(training_data, expected):

	# initial weights 
	w = random.rand(64)

	errors = [] # stores error values for plotting
	learning_rate = 0.1 # learning_rate normally < 0.1
	number_of_learning_iterations = 1500


	# learning through iterative optimazing, slide 25
	for i in xrange(number_of_learning_iterations): 
		x = choice(training_data) # random input set from the training data
		scalar_product = dot(w, x) # calc scalar product
		error = expected - activation_function(scalar_product)
		errors.append(error) # for plotting
		w += learning_rate * error * x # correct weight so that Φ(x) nears expected

	# print it
	for x in training_data: 
		scalar_product = dot(x, w) 
		print("{}: {} -> {}".format(x[:2], scalar_product, activation_function(scalar_product)))

	# plot it
	ylim([-1,1]) 
	plot(errors)
	savefig('plot.png')


if __name__ == '__main__':

	# optdigits.tra = Trainingsmenge in textform. Jede Zeile = 1 Beispiel. Jede Zeile hat 65 Spalten. 1 - 64 Merkmalsvektor, 65 Label (0-9)
	# optdigits.tes = Eine weitere Trainingsmenge, aufgebaut wie tra
	# optdigits.names = Weitere Details

	# Trainingsmenge einlesen
	#training_data = [ map(array, x.split()) for x in file('optdigits.tra').readlines() ]

	training_data = [ map(int,x.split(',')) for x in file('optdigits.tra').readlines() ]
	label2_data = []
	
	for x in training_data:
		if (x[-1:][0] == 2): # if label == 2
			label2_data.append(x[:-1]) # ohne label anhaengen

	#print label2_data[:5]

	main( map(array, label2_data), 2)
	













	