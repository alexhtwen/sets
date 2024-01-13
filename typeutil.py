def is_hashable(obj: object) -> bool:
    """
    Check if an object is hashable.

    Args:
    obj (object): The object to check.

    Returns:
    bool: True if the object is hashable, False otherwise.
    """
    return_value: bool = True
    try:
        hash(obj)
    except TypeError:
        return_value = False
    finally:
        return return_value


# print(f'{is_hashable(1) = }')
# print(f'{is_hashable(3.14) = }')
# print(f'{is_hashable('A') = }')
# print(f'{is_hashable('A'*99999) = }')
# print(f'{is_hashable(99**99) = }')
# print(f'{is_hashable([]) = }')
# print(f'{is_hashable([5, 6, 8]) = }')
# print(f'{is_hashable(()) = }')
# print(f'{is_hashable((5,)) = }')
# print(f'{is_hashable(set()) = }')
# print(f'{is_hashable({8, 6}) = }')
# print(f'{is_hashable({}) = }')
# print(f'{is_hashable({'id': 1, 'scores': [85, 71, 59, 70, 92]}) = }')
# print(f'{is_hashable(True) = }')
# print(f'{is_hashable(False) = }')
# print(f'{is_hashable(None) = }')
