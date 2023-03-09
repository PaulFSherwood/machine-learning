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
# Video: Neural Networks from Scratch - P.3 The Dot Product
# Website: https://www.youtube.com/watch?v=tMrbN67U9d4&list=PLQVvvaa0QuDcjD5BAw2DxE6OF2tius3V3&index=6
# Date: March 8th, 2023
# Purpose: Machine Learning training
#
# Notes:
# - This script requires Python 3.7 or later.
# - Make sure to install the necessary dependencies before running.
####################################################################################

inputs = [1, 2, 3, 2.5]

weights = [
            [0.2, 0.8, -0.5, 1.0],
            [0.5, -0.91, 0.26, -0.5],
            [-0.26, -0.27, 0.17, 0.87]
            ]

biases = [2, 3, 0.5]

layer_outputs = [] # Output of current layer
for neuron_weights, neuron_bias in zip(weights, biases):
    neuron_output = 0 # Output of given neuron
    for n_input, weight in zip(inputs, neuron_weights):
        neuron_output += n_input * weight
    neuron_output += neuron_bias
    layer_outputs.append(neuron_output)

print(layer_outputs)