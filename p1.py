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