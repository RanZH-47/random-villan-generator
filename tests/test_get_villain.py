from random_villan_generator.get_villain import get_villain
from random_villan_generator.villains import villains


def test_get_villain_name():
    """
    GIVEN
    WHEN get_villain is called
    THEN random villain name from villain name list is returned
    """
    villain = get_villain()
    assert villain in villains
