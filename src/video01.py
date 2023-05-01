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
# Video: Neural Networks from Scratch - P.1 The Dot Product
# Website: https://www.youtube.com/watch?v=Wo5dMEP_BbI&list=PLQVvvaa0QuDcjD5BAw2DxE6OF2tius3V3&index=1
# Date: March 8th, 2023
# Purpose: Machine Learning training
#
# Notes:
# - This script requires Python 3.7 or later.
# - Make sure to install the necessary dependencies before running.
####################################################################################

import sys
import numpy as np
import matplotlib
                                                #########################################
                                                # class versions    # user versions     #
print("Python: ", sys.version)                  # Python: 3.7.7     # Python: 3.9.7     #
print("Numpy: ", np.__version__)                # Numpy: 1.18.2     # Numpy: 1.24.1     #
print("Matplotlib: ", matplotlib.__version__)   # Matplotlib: 3.2.1 # Matplotlib: 3.6.3 #
                                                #########################################

# Program start
inputs = [1.2, 5.1, 2.1]
weights = [3.1, 2.1, 8.7]
bias = 3

output = inputs[0] * weights[0] + inputs[1] * weights[1] + inputs[2] * weights[2] + bias
print(output)