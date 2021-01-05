import numpy as np
from alpha_rank import alpha_rank
from functools import partial
import time


# Used for profiling the alpha rank implementation when used repeatedly
if __name__ == "__main__":
    N = 8
    P = 1

    alpha = partial(alpha_rank, use_inf_alpha=True, inf_alpha_eps=0.0000001, use_sparse=True if N**P >= 25 else False)

    K = 5000
    print("Starting {:,} iterations.".format(K))

    # Crude timing, but its sufficient
    start_time = time.time()
    for i in range(K):
        if i % (K // 10) == 0:
            print("Iteration", i)
        payoff = np.random.random(size=(P, N, N))
        phi = alpha(payoff)
        n_phi = phi + 1 # Double checking phi is being used
    end_time = time.time()

    print("Took {:,} seconds.".format(end_time - start_time))