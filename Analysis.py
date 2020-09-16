import matplotlib.pyplot as plt
import numpy as np
import random

class Analysis:
    def __init__(self, adj, fileName) -> None:
        # Store adjacency matrix (estimated)
        ########################################################################
        self.fileName = fileName
        self.adj = adj
        degree_sorted = self.adj.sum(1) # scipy.sparse.lil_matrix.sum(axis)
        degree_sorted = np.squeeze(np.array(degree_sorted))
        # print("Degree_sorted: ", degree_sorted)
        degree_count = self.counter(degree_sorted)
        print("Degree counted: ", degree_count)
        self.degrees = degree_count
        # self.degrees = dict((np.log(k), np.log(v)) for k, v in degree_count.items())
        print("Degree counted (log): ", self.degrees)

    def counter(self, degree_sorted):
        degree_count = {}
        for node in degree_sorted:
            if node in degree_count:
                degree_count[node] += 1
            else:
                degree_count[node] = 1
        return degree_count

    def plotDegDist(self):
        plt.scatter(self.degrees.keys(), self.degrees.values())
        plt.xlabel('Degree')
        plt.ylabel('Count')
        plt.xscale('log')
        plt.yscale('log')
        plt.xlim([max(min(self.degrees.keys()) - 10, 0.5), max(self.degrees.keys()) + 100])
        plt.savefig(self.fileName)