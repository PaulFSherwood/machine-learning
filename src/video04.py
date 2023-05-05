####################################################################################
#  __  __            _     _            
# |  \/  | __ _  ___| |__ (_)_ __   ___ 
# | |\/| |/ _` |/ __| '_ \| | '_ \ / _ \
# | |  | | (_| | (__| | | | | | | |  __/
# |_|  |_|\__,_|\___|_| |_|_|_| |_|\___|                                      
#  _                          _             
# | |    ___  __ _ _ __ _ __ (_)_ __   __ _ 
# | |   / _ \/ _` | '__| '_ \| | '_ \ / _` |
# | |__|  __/ (_| | |  | | | | | | | | (_| |
# |_____\___|\__,_|_|  |_| |_|_|_| |_|\__, |
#                                     |___/ 
#
# Author: Sentdex
# Video: Neural Networks from Scratch - P.4 Batches, Layers, and Objects
# Website: https://www.youtube.com/watch?v=TEWy9vZcxW4&list=PLQVvvaa0QuDcjD5BAw2DxE6OF2tius3V3&index=4
# Date: May 1st, 2023
# Purpose: Machine Learning training
#
# Educational Notes:
# - Batches
# - Layers
# - Objects
#
####################################################################################

import numpy as np

np.random.seed(0)

# inputs = [[1, 2, 3, 2.5],
#           [2.0, 5.0, -1.0, 2.0],
#           [-1.5, 2.7, 3.3, -0.8]]

# weights = [
#             [0.2, 0.8, -0.5, 1.0],
#             [0.5, -0.91, 0.26, -0.5],
#             [-0.26, -0.27, 0.17, 0.87]
#             ]

# biases = [2, 3, 0.5]

# weights2 = [
#             [0.1, -0.14, .5],
#             [-0.5, 0.12, -0.33],
#             [-0.44, 0.73, -0.13]
#             ]

# biases2 = [-1, 2, -0.5]

# # dot product of two vectors results in a scalar value
# layer1_outputs = np.dot(inputs, np.array(weights).T) + biases
# print(layer1_outputs)


# layer2_outputs = np.dot(layer1_outputs, np.array(weights2).T) + biases2
# print(layer2_outputs)

X = [[1, 2, 3, 2.5],
     [2.0, 5.0, -1.0, 2.0],
     [-1.5, 2.7, 3.3, -0.8]]

class layer_Dense:
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.10 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))
    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases

layer1 = layer_Dense(4, 5)
layer2 = layer_Dense(5, 2)

layer1.forward(X)
# print(layer1.output)

layer2.forward(layer1.output)
print(layer2.output)
