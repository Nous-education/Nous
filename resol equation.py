from sympy import simplify, Eq, solve, symbols
import numpy as np
x = symbols('x')

#entré utilisateur
a = input("coté droit  = ")
b = input("côté gauche = ")

#adap library
a_expr = simplify(a)
b_expr = simplify(b)

#résolution
solution = solve(Eq(a_expr, b_expr), x)

#renvoiyer

print("Solution pour x :", solution)
