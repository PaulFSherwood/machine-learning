import numpy as np

layer_output = [4.8, 1.21, 2.385]

E = 2.71828182846

exp_values = np.exp(layer_output) #[]

# for output in layer_output:
#     exp_values.append(E ** output)

print(exp_values)

norm_base = sum(exp_values)
norm_values = []

for value in exp_values:
    norm_values.append(value / norm_base)

print(norm_values)
print(sum(norm_values))