from sympy import *

dx = [


    2.0019,

    4.36821,

    7.78768,

    10.46436,

    13.95557,
    17.30696,

    21.38322,

    19.97862,

    22.76828,
    25.33573,



]

dy = [


    3.15561,

    3.67144,
    3.98231,

    3.87572,
    3.69437,
    3.88595,
    4.08581,
    4.03642,
    4.04956,
    3.72302,


]


def find_lagrange_polynomial(total_node, target_node, lx, ly):
    if total_node == target_node:
        return find_lagrange_polynomial(total_node - 1, target_node, lx, ly)

    if total_node < 0:
        return 1
    x = Symbol("x")
    return Mul((x - lx[total_node])
               * find_lagrange_polynomial(total_node - 1, target_node, lx, ly),
               Pow((lx[target_node] - lx[total_node]), -1))


def find_function(n, lx, ly):
    expr = 0
    for i in range(n):
        x = Symbol("x")
        expr = Add(expr, ly[i] * find_lagrange_polynomial(n - 1, i, lx, ly))

    return expr


print(expand(find_function(len(dy), dx, dy)))
