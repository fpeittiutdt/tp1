import json
from typing import List
import matplotlib.pyplot as plt

def readJSON(instance: str) -> json:
    with open('../../data/{}.json'.format(instance)) as f:
        instance = json.load(f)
        return instance

def saveJSON(instance: str, data: json):
    with open('./solutions/{}.json'.format(instance), 'w') as f:
        json.dump(data, f)

def saveSolution(instance:str, x:List[float], y:List[float], best:float):
    
    return

def plot_pwl(solution, color='g'):
    for i in range(solution['n'] - 1):
        plt.plot([solution['x'][i], solution['x'][i+1]], [solution['y'][i], solution['y'][i+1]], color=color)


def plot_data(data, color='k'):
    plt.plot(data['x'], data['y'],'.', color=color)