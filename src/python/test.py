import utils.algorithms as algorithms
import utils.utils as utils
import matplotlib.pyplot as plt
import numpy as np
import json

'''
Posible ejemplo (para la instancia titanium) de formato de solucion, y como exportarlo a JSON.
La solucion es una lista de tuplas (i,j), donde:
	i: indica el indice del punto de la discretizacion de la abscisa.
	j: indica el indice del punto de la discretizacion de la ordenada.
 
----------------------------------------------------------------------------------------------

Represetnamos la solucion con un diccionario que indica:
    n: Cantidad de breakpoints.
    x: Lista con las coordenadas de la abscisa para cada breakpoint.
    y: Lista con las coordenadas de la ordenada para cada breakpoint.
'''

DATA: json = {
    'ASPEN': 'aspen_simulation',
    'ETHANOL': 'ethanol_water_vle',
    'OPTIMISTIC': 'optimistic_instance',
    'TITANIUM': 'titanium',
    'TOY': 'toy_instance',
}

def graph(instance: str, solution, m:int, n:int):
    data: json = utils.readJSON(DATA[instance])
    grid_x = np.linspace(min(data['x']), max(data['x']), num=m, endpoint=True)
    grid_y = np.linspace(min(data['y']), max(data['y']), num=n, endpoint=True)
 
    sol = {
        'x': [grid_x[seg[0]] for seg in solution],
        'y': [grid_y[seg[1]] for seg in solution]
    }
    
    print('\nX: {}\nY: {}'.format(data['x'], data['y']))
    print('\n\nSOLUTION\nX: {}\nY: {}'.format(sol['x'], sol['y']))
    
    plt.scatter(data['x'], data['y'], label='Instance')
    plt.plot(sol['x'], sol['y'], color='red', linestyle='-', marker='o', label='PWL')
    plt.title('{} with PWL'.format(instance))
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.legend()
    plt.grid(True)
    plt.show()
    

def main():
    graph(instance='TITANIUM', solution=[(0, 0), (1, 0), (2, 0), (3, 2), (4, 0), (5, 0)], m=6, n=6)

if __name__ == '__main__':
    main()
