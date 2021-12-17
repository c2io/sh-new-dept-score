from typing import Tuple, List
from dataclasses import dataclass


@dataclass
class ConditionScore:
    conditions: Tuple
    scores: Tuple
    temp: List


def test_2_obj():
    a = ConditionScore([1, 2, 3], [2, 3, 4], [3])
    b = ConditionScore([3, 2, 3], [4, 3, 4], [])

    assert a.conditions == [1, 2, 3]
    assert b.scores == [4, 3, 4]

    a.temp.append(3)
    assert a.temp == [3, 3]
