

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    try:
        assert len(height) == len(weight), "lenghts are not equal"
        assert isinstance(height[0], (int, float)), "height needs to contain either int or float values"
        assert isinstance(weight[0], (int, float)), "weight needs to contain either int or float values"
        assert 0 not in height, "height needs to have only positive values"
    except AssertionError as exception:
        print(f"{exception.__class__.__name__}: {exception}")
        return []
    return [w / h**2 for h, w in zip(height, weight)]

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    if not bmi:
        return []
    try:
        assert isinstance(bmi[0], (int, float)), "bmi needs to contain either int or float values"
    except AssertionError as exception:
        print(f"{exception.__class__.__name__}: {exception}")
        return []
    return [number > limit for number in bmi]


