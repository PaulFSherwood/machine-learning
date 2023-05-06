# import numpy as np
# import math



# # INPUT
# layer_output = [4.8, 1.21, 2.385]

# # E = 2.71828182846
# E = math.e

# # EXPONENTIATE
# exp_values = np.exp(layer_output) #[]

# # for output in layer_output:
# #     exp_values.append(E ** output)

# print(exp_values)

# norm_base = sum(exp_values)
# norm_values = []

# # I think this normalizes the values
# print("Norm Base:", norm_base)
# for value in exp_values:
#     print("Value:", value)
#     print("Norm Base:", norm_base)
#     norm_values.append(value / norm_base)
#     print("Norm Value:", norm_values)
#     print("\n")

# # NORMALIZE
# norm_values = exp_values / np.sum(exp_values)

# # EXPONENTIATION AND NORMALIZATION = SOFTMAX


# print(norm_values)
# print(sum(norm_values))

import numpy as np
import nnfs

nnfs.init()

# SOFTMAX FUNCTION
# INPUT - EXPONENTIATE - NORMALIZE - OUTPUT
# OR 
# INPUT - SOFTMAX - OUTPUT

# INPUT
layer_ouputs = [[4.8, 1.21, 2.385],
                [8.9, -1.81, 0.2],
                [1.41, 1.051, 0.026]]

####################
## SOFTMAX START

# EXPONENTIATE
exp_values = np.exp(layer_ouputs)

#      AXIS = 0 - SUMS THE COLUMNS
#      AXIS = 1 - SUMS THE ROWS
# KEEP DIMS = TRUE - KEEPS THE DIMENSIONS OF THE ARRAY
# print(np.sum(layer_ouputs, axis=1, keepdims=True))

# NORMALIZE
norm_values = exp_values / np.sum(exp_values, axis=1, keepdims=True)

## SOFTMAX END
####################

# OUTPUT

print(norm_values)
# print(sum(norm_values))

# print(np.exp(1))    # E ^ 1 = 2.71828182846
# print(np.exp(10))   # E ^ 10 = 22026.4657948
# print(np.exp(100))  # E ^ 100 = 2.68811714182e+43
# print(np.exp(1000)) # E ^ 1000 = inf