# pool_ops.py

# Usage: python3 pool_ops.py c_in h_in w_in h_pool w_pool s p

import sys
import math

# Arguements 
# c_in: input channel count
# h_in: input height count
# w_in: input width count
# n_filt: number of filters in the convolution layer
# h_filt: filter height count
# w_filt: filter width count
# s: stride of convolution filters
# p: amount of padding on each of the four input map sides

# Parse script arguments
if len(sys.argv) == 8:
    c_in = int(sys.argv[1])
    h_in = int(sys.argv[2])
    w_in = int(sys.argv[3])
    h_pool = int(sys.argv[4])
    w_pool = float(sys.argv[5])
    s = float(sys.argv[6])
    p = float(sys.argv[7])
else:
    print('Usage: python3 pool_ops.py c_in h_in w_in h_pool w_pool s p')
    exit()


# Height of the output
h_out = [(h_in+2*p-h_pool)/s +1]

# Width of the output
w_out = [(w_in+2*p-w_pool)/s +1]

#Total number of divisions
divs = c_in*h_out*w_out

# total number of additions
adds = divs*(h_pool*w_pool-1)

c_out = c_in

muls = 0

print(int(c_out)) # output channel count
print(int(h_out)) # output height count
print(int(w_out)) # output width count
print(int(adds))  # number of additions performed
print(int(muls))  # number of multiplications performed
print(int(divs))  # number of divisions performed