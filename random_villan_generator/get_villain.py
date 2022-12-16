import random
from random_villan_generator.villains import villains

def get_villain() -> dict:
    villain_picked = random.choice(villains)
    return villain_picked