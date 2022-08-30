from statistics import mean, variance
from unicodedata import decimal
import numpy as np
mylist = [2, 6, 2, 8, 4, 0, 1, 5, 7]


def calculate(mylist):
    if len(mylist) < 9:
        raise ValueError("List must contain nine numbers.")
    else:
        a = np.array(mylist)
        a = a.reshape(3, 3)
        sum_list = [list(a.sum(axis=0)), list(
            a.sum(axis=1)), sum(a.reshape(-1))]
        max_list = [list(a.max(axis=0)), list(
            a.max(axis=1)), max(a.reshape(-1))]
        min_list = [list(a.min(axis=0)), list(
            a.min(axis=1)), min(a.reshape(-1))]
        mean_list = [list(a.mean(axis=0)), list(
            a.mean(axis=1)), np.mean(a.flatten())]
        std_list = [list(a.std(axis=0)), list(
            a.std(axis=1)), a.reshape(-1).std()]
        var_list = [list(a.var(axis=0)), list(a.var(axis=1)), a.var()]
        calculations = {'mean': mean_list, 'variance': var_list,
                        'standard deviation': std_list, 'max': max_list, 'min': min_list, 'sum': sum_list}
        return calculations


print(calculate([2, 6, 2, 8, 4, 0, 1, 5, 7]))
