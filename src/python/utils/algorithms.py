from typing import *
import json

BIG_NUMBER = 1e10 # Check if needed.

def e(x: float, y: float):
    
    return

def y(x: Tuple[float, float], y: Tuple[float,float]):
    
    return

def line(t_prime, y_prime, t_double_prime, y_double_prime, t):
    """
    Calcula la recta que une dos puntos dados.
    """
    
    return ((y_double_prime - y_prime) / (t_double_prime - t_prime)) * (t - t_prime) + y_prime

def absolut_error(xi, yi, t_prime, y_prime, t_double_prime, y_double_prime):
    """
    Calcula el error absoluto de aproximación por la recta en el punto xi.
    """
    y_predicho = line(t_prime, y_prime, t_double_prime, y_double_prime, xi)
    return abs(yi - y_predicho)


'''
Para el primer segmento, 1 = 595, r2 = 787, y la pieza f1(t) se obtiene mediante la función lineal 
que une los puntos (595,0.601) y (787,0.601), siguiendo la ecuación (1). Análogamente, la pieza f2(t) 
tiene dominio [r2, r3] = [787, 883] y la función f2(t) se obtiene aplicando la ecuación (1) tomando
como referencia los puntos (787, 0.601) y (883, 1.228). Notar que una función continua PWL
puede ser definida en términos de K puntos dados por (rk, fk(rk)) para k = 1, . . . , K - 1 y
(rK, fK-1(rK)).
Finalmente, analizamos el error de la aproximación. Dada una pieza fk(t) definida por los
breakpoints (rk, zk) y (rk+1, zk+1) y los puntos (xi
, yi), i = 1, . . . , n, definimos el error de
aproximación de la pieza k-ésima como la suma de los errores de los puntos (xi
, yi) tal que
xi ∈ (rk, rk+1], es decir,

'''

def brute(instance: json) -> List[Tuple[int, int]]:
    for x, y in zip(instance['x'], instance['y']):
        # error = absolut_error(xi, yi, t_prime, y_prime, t_double_prime, y_double_prime)

        print('X: {} Y: {}'.format(x, y))
    return [(0, 0), (1, 0), (2, 0), (3, 2), (4, 0), (5, 0)]

def backtrack(instance: json) -> List[Tuple[int, int]]:
    return []

def dynamic(instance: json) -> List[Tuple[int, int]]:
    return []