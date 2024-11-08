import main
import io
import sys
import re
import math
import types


def test_main_1():
    sc1 = [100, 100, 100]
    sc2 = [90, 90, 90]

    s1 = main.Student('James', sc1)
    s2 = main.Student('Mary', sc2)
    print(s1)
    print(s2)
    print(f'Total number of students: {main.Student.numofStudent}')

    assert callable(s1.__gt__) == True
    assert callable(s1.__lt__) == True
    assert callable(s1.__sub__) == True
    assert callable(s1.__str__) == True


def test_main_2():
    sc1 = [100, 100, 100]
    sc2 = [90, 90, 90]

    s1 = main.Student('James', sc1)
    s2 = main.Student('Mary', sc2)
    print(s1)
    print(s2)
    print(f'Difference between s1 and s2 scores: {s1-s2}')

    print(s1 > s2)
    print(s1 < s2)

    assert (s1 > s2) == True
    assert (s1 < s2) == False
    assert (s1 - s2) == 10.0
