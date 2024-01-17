import numpy as np

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    try :

        assert all(type(w) == int or type(w) == float for w in weight), "Error: Weight Type Error"
        assert all(type(h) == int or type(h) == float for h in height), "Error: Height Type Error"

        assert(len(height) == len(weight)), "Error: Height and Weight must have the same length"
        
        return (np.array(weight) / (np.array(height) ** 2)).tolist()

    except AssertionError as error:
        print(error)
        return []


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    assert all(type(b) == int or type(b) == float for b in bmi), "Error: bmi Type Error"
    assert type(limit) == int, "Error: bmi Type Error"
    return (np.array(bmi) > limit).tolist()

