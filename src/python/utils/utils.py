import json
from typing import List

def readJSON(instance: str) -> json:
    with open('../../data/{}.json'.format(instance)) as f:
        instance = json.load(f)
        return instance

def saveJSON(instance: str, data: json):
    with open('./solutions/{}.json'.format(instance), 'w') as f:
        json.dump(data, f)

def saveSolution(instance:str, x:List[float], y:List[float], best:float):
    
    return