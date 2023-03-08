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
# Video: Neural Networks from Scratch - P.2 Coding a Layer
# Website: https://www.youtube.com/watch?v=lGLto9Xd7bU&list=PLQVvvaa0QuDcjD5BAw2DxE6OF2tius3V3&index=2
# Date: March 8th, 2023
# Purpose: Machine Learning training
#
# Notes:
# - This script requires Python 3.7 or later.
# - Make sure to install the necessary dependencies before running.
####################################################################################

inputs = [1, 2, 3, 2.5]

weights1 = [0.2, 0.8, -0.5, 1.0]
weights2 = [0.5, -0.91, 0.26, -0.5]
weights3 = [-0.26, -0.27, 0.17, 0.87]

bias1 = 2
bias2 = 3
bias3 = 0.5

output = [inputs[0] * weights1[0] + inputs[1] * weights1[1] + inputs[2] * weights1[2] + inputs[3] * weights1[3] + bias1,
          inputs[0] * weights2[0] + inputs[1] * weights2[1] + inputs[2] * weights2[2] + inputs[3] * weights2[3] + bias2,
          inputs[0] * weights3[0] + inputs[1] * weights3[1] + inputs[2] * weights3[2] + inputs[3] * weights3[3] + bias3]

# output = sum(x * w for x, w in zip(inputs, weights)) + bias

print(output)