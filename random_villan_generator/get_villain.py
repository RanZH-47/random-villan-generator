import random

from random_villan_generator.villains import villains


def get_villain() -> dict:
    """
    Get a villain.

    :return: selected villain
    :rtype: dict
    """
    villain_picked = random.choice(villains)
    return villain_picked
