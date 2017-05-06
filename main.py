import numpy
import matplotlib.pyplot as plt

from FunctionBox import FunctionBox
import timeit

from Solver import Solver

x_points = []
y_points = []

def power_list(n):
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
    res = count_time(function, 1, 4, 10, 7, 1)
    x.append(res[0])
    y.append(res[1])

    return (x_points, y_points)

if __name__ == '__main__':
    function_box = FunctionBox()

    res = points_generator(power_list)
    n2_ap = function_box.n2(res)
    n_ap = function_box.n(res)
    s_ap = function_box.s(res)

    y2 = [n2_ap(x) for x in res[0]]
    y = [n_ap(x) for x in res[0]]
    ys = [s_ap(x) for x in res[0]]

    function_details = {}
    function_details["x"] = res[0]

    function_details["n2_function"] = n2_ap
    function_details["n2_y"] = y2
    function_details["n_function"] = n_ap
    function_details["n_y"] = y
    function_details["s_function"] = s_ap
    function_details["s_y"] = ys


    solver = Solver(function_details)
    solver.solve()
    plt.plot(res[0], res[1], 'ro', res[0], y2, "g^", res[0], y, "b--", res[0], ys )
    plt.xscale('log')
    plt.yscale('log')
    plt.ylabel('some numbers')
    plt.show()
