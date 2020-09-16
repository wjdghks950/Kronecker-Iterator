import numpy as np
from scipy.sparse import lil_matrix
import time

class KProds:
    def __init__(self,  k: int, filePath: str) -> None:
        self.k = k # The number of Kronecker products
        # Load the inital matrix from the file
        # You may declare any class variables if needed                        #
        ########################################################################
        assert self.k > 0
        try:
            self.kron_init = np.loadtxt(filePath, dtype="int8")
        except OSError as e:
            print("Unexpected Error occurred while reading in ", filePath, " ERR_NUM: ", e.errno)
        finally:
            print("Kronecker Initiator => \n {} \nShape: {}".format(self.kron_init, self.kron_init.shape))

    def produceGraph(self) -> lil_matrix:
        '''
        Iterative Implementation of Kronecker Graph Iterator
        '''
        # Compute the k-th Kronecker power of the inital matrix
        ########################################################################
        N_0 = self.kron_init.shape[0]
        for k_step in range(1, self.k + 1):
            if k_step < 2:
                kronecker_prev = lil_matrix(self.kron_init)
            else:
                N_k_prev = kronecker_prev.shape[0]
                N_k = N_0 ** k_step
                kronecker_out = lil_matrix((N_k, N_k), dtype="int8") # Memory allocation fails when dtype="int64"
                print(kronecker_out.shape)
                for row_init in range(N_0):
                    row_start = N_k_prev * row_init
                    row_end = row_start + N_k_prev
                    for col_init in range(N_0):
                        col_start = N_k_prev * col_init
                        col_end = col_start + N_k_prev
                        if self.kron_init[row_init][col_init] != 0:
                            kronecker_out[row_start:row_end, col_start:col_end] = kronecker_prev
                        else:
                            kronecker_out[row_start:row_end, col_start:col_end] = lil_matrix((N_k_prev, N_k_prev), dtype="int8")
                if k_step != self.k:
                    kronecker_prev = kronecker_out.copy()
                    if not isinstance(kronecker_prev, lil_matrix):
                        kronecker_prev = lil_matrix(kronecker_prev)
                    del kronecker_out  # Relieve memory
        print("OUT: ", kronecker_out.toarray())
        print("k = {} / OUT (shape) = {}: ".format(self.k, kronecker_out.shape))
        # kronecker_sparse = lil_matrix(kronecker_out, dtype="int8")
        return kronecker_out

'''
Recursive Implementation of Kronecker Graph Iterator
'''
#     def produceGraph(self) -> lil_matrix:
#         # Compute the k-th Kronecker power of the inital matrix
#         ########################################################################
#         kronecker_out = kronecker(self.kron_init, self.k)
#         print("OUT: ", kronecker_out)
#         print("k = {} / OUT (shape): ".format(self.k, kronecker_out.shape))
#         kronecker_sparse = lil_matrix(kronecker_out)
#         return kronecker_out

# def kronecker(kron_init, k):
#     if k <= 1:
#         return kron_init
#     else:
#         # TODO: Need more efficient implementation!
#         # kronecker(k-1) * kron_init
#         kronecker_prev = kronecker(kron_init, k-1)
#         N_k = len(kronecker_prev)
#         N_0 = len(kron_init)
#         out = []
#         count = 0
#         for row_k in range(N_k):
#             for row_init in range(N_0):
#                 out.append([])
#                 for kron_elem in kronecker_prev[row_k]:
#                     if kron_elem == 0:
#                         out[count] += ([0] * N_0)
#                     else:
#                         for init_elem in kron_init[row_init]:
#                             out[count].append(kron_elem * init_elem)
#                 count += 1
#         out = np.array(out)
#         return out