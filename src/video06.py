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

# # norm_base = sum(exp_values)
# # norm_values = []

# # for value in exp_values:
# #     norm_values.append(value / norm_base)

# # NORMALIZE
# norm_values = exp_values / np.sum(exp_values)

# # EXPONENTIATION AND NORMALIZATION = SOFTMAX


# print(norm_values)
# print(sum(norm_values))

import numpy as np
import nnfs

nnfs.init()

layer_ouputs = [[4.8, 1.21, 2.385],
                [8.9, -1.81, 0.2],
                [1.41, 1.051, 0.026]]

exp_values = np.exp(layer_ouputs)

# print(np.sum(layer_ouputs, axis=1, keepdims=True))

norm_values = exp_values / np.sum(exp_values, axis=1, keepdims=True)

print(norm_values)
# print(sum(norm_values))