import numpy
import matplotlib.pyplot as plt

from FunctionBox import FunctionBox
import timeit

from Solver import Solver

x_points = []
y_points = []

def power_list(n):
    for i in numpy.arange(0,n):
        for j in numpy.arange(0,n):
            pass

def count_time(function, start_a, start_b, stop_a, stop_b, step):
    x = []
    y = []
    for b in range(start_b, stop_b):
        print(b)
        for a in numpy.arange(start_a, stop_a, step):
            x = a * (10 ** b)
            x_points.append(x)
            arg = "main." + function.__name__ + "(" + str(x) + ")"
            t = timeit.Timer(stmt = arg, setup = "import main")
            y = min(t.repeat(1,1))
            y_points.append(y)

            print(x, " ", y)
    return (x,y)

def points_generator(function):

    x = []
    y = []
    res = count_time(function, 1, 1, 10, 4, 0.2)
    x.append(res[0])
    y.append(res[1])
    # res = count_time(function, 1, 4, 10, 7, 1)
    # x.append(res[0])
    # y.append(res[1])

    return (x_points, y_points)

if __name__ == '__main__':

    res = points_generator(power_list)

    solver = Solver(res)
    solver.solve()
