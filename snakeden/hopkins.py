from random import random
from sklearn.neighbors import KDTree
from numpy import array, ndarray
from scipy.stats import f

class Hopkins:
    def __init__(self, data:ndarray, area_width:int, area_height:int, random_data:ndarray = None) -> None:
        self.N = len(data)
        self.X = data
        self.x_random = random_data
        self.area_width = area_width
        self.area_height = area_height
        self.tree = KDTree(self.X)
        self.H = self._hopkins_statistic()

    def _squared_s_distances(self):
        distances, indices = self.tree.query(self.X, k=2)
        return sum([x**2 for x in distances[:,1]])

    def _squared_r_distances(self):
        if self.x_random.all() == None:
            random_points = [(self.area_width*random(), self.area_height*random()) for _ in range(self.N)]
            self.x_random = array(random_points)
        distances, indices = self.tree.query(self.x_random, k=1)
        return sum([x**2 for x in distances[:,0]])

    def _hopkins_statistic(self):
        s_dist_squared = self._squared_s_distances()
        r_dist_squared = self._squared_r_distances()
        print(s_dist_squared, r_dist_squared)
        return r_dist_squared/s_dist_squared

    def H_statistic(self) -> float:
        return self.H

    def critical_values(self, significance=0.05) -> tuple:
        a = significance/2
        dist = f(2*self.N, 2*self.N)
        return (dist.ppf(a), dist.ppf(1-a))
