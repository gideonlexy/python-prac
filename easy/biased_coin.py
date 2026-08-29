import random

random.seed(0)

def biased_coin_flip(input):
    p = input["probability"]
    N = input["N"]
    outcomes = [0,1]
    probablities = [1-p, p]
    
    results = random.choices(outcomes, probablities, k=N)
    return results