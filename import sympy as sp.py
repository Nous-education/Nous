import sympy as sp # type: ignore
from sympy import symbols, Eq, solve,simplify # type: ignore
def résolution (a_str,b_str):
    x = symbols('x')

    try:
        a_expr = simplify(a_str.replace('^','**'))
        b_expr = simplify(b_str.replace('^','**'))

        equation = Eq (a_expr,b_expr)
        solution = solve (equation, x)

        if not solution :
            return "L'équation n'a pas de solution"
        elif len(solution) == 1:
            return f"solution : x  = {solution}"
        else :
            return "no solution"
        
        



