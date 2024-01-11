# from typeutil import is_hashable

class RobustSet(set):
    # def __init__(self, s: set):
    #     super().__init__()
    #     self.__set = s

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

    def __init__(self, s: set):
        super().__init__(s)  # Initialize the set with elements of s

    # modified methods
    # OK
    def add(self, *elements: object) -> int:
        '''
        新增的元素如果是unhashable，不會產生exception而是略過。
        可以一次新增多個values，也允許不傳入參數(即不新增)。
        傳回值: int，代表實際新增的元素個數。
        '''
        # if not elements:
        #     return 0
        self_bak = self.copy()
        for element in [element for element in elements if RobustSet.is_hashable(element)]:
            super().add(element)
        return len(self) - len(self_bak)

    def remove(self, *elements: object) -> int:
        '''
        可以一次刪除多個values，也允許不傳入參數(即不刪除)。
        欲刪除元素為unhashable或不在原set中，都不會產生exception。
        傳回值: int，代表實際刪除的元素個數。
        '''
        # if not elements:
        #     return 0
        self_bak = self.copy()
        # if set(hashable_elements := [element for element in elements if RobustSet.is_hashable(element)]).issubset(self):
        #     return_value = True
        # else:
        #     return_value = False
        for element in elements:
            if RobustSet.is_hashable(element):
                super().discard(element)
        return len(self_bak) - len(self)

    def discard(self, *elements: object) -> None:
        '''
        可以一次刪除多個values，亦允許不傳入參數。
        欲刪除元素為unhashable時不會產生exception。
        傳回值: None
        '''
        for element in elements:
            if RobustSet.is_hashable(element):
                super().discard(element)
        return None

    def pop(self) -> object:
        """
        Remove and return an arbitrary set element.
        If the set is empty, do nothing and return None.

        Returns:
            The removed element if the set is not empty, otherwise None.
        """
        import random
        if not self:  # Check if the set is empty
            return None
        self_t = tuple(self)
        return super().remove(self_t[random.randint(0, len(self_t) - 1)])
        # return super().pop()  # Use the superclass's pop method

    # unmodified methods
    # def isdisjoint(self, other):    # 以string literal作為傳回值的type hint
    #     print(f'{other = }')
    #     return RobustSet(super().isdisjoint(other))

    # def issubset(self, other):
    #     return RobustSet(super().issubset(self, other))

    # def issuperset(self, other):
    #     return RobustSet(super().issuperset(self, other))

    # def union(self, *others):
    #     return RobustSet(super().union(self, *others))

    # def intersection(self, *others):
    #     return RobustSet(super().intersection(self, *others))

    # def difference(self, *others):
    #     return RobustSet(super().difference(self, *others))

    # def symmetric_difference(self, other):
    #     return RobustSet(super().symmetric_difference(self, other))

    # def update(self, *others):
    #     return RobustSet(super().self, *others)

    # def intersection_update(self, *others):
    #     return RobustSet(super().intersection_update(self, *others))

    # def difference_update(self, *others):
    #     return RobustSet(super().difference_update(self, *others))

    # def symmetric_difference_update(self, other):
    #     return RobustSet(super().symmetric_difference_update(self, other))

    # def clear(self):
    #     # return RobustSet(super().clear())
    #     super().clear()
    #     return self

    # new methods
    def replace(self, old: object, new: object) -> bool:
        '''New method'''
        if RobustSet.is_hashable(old) and RobustSet.is_hashable(new) and (old in self) and (old != new):
            self.remove(old)
            self.add(new)
            return_value = True
        else:
            return_value = False
        return return_value

    # def show(self):
    #     '''New method'''
    #     return self

    # operators
    # def __or__(self, other: set) -> 'RobustSet':
    #     # Override union operation
    #     return RobustSet(super().__or__(self, other))

    # def __and__(self, other: set) -> 'RobustSet':
    #     # Override intersection operation
    #     return RobustSet(super().__and__(self, other))

    # def __sub__(self, other: set) -> 'RobustSet':
    #     # Override difference operation
    #     return RobustSet(super().__sub__(self, other))

    # def __xor__(self, other: set) -> 'RobustSet':
    #     # Override symmetric difference operation
    #     return RobustSet(super().__xor__(self, other))

    # def __le__(self, other: set) -> bool:
    #     # Override subset operation
    #     return super().__le__(self, other)

    # def __lt__(self, other: set) -> bool:
    #     # Override proper subset operation
    #     return super().__lt__(self, other)

    # def __ge__(self, other: set) -> bool:
    #     # Override superset operation
    #     return super().__ge__(self, other)

    # def __gt__(self, other: set) -> bool:
    #     # Override proper superset operation
    #     return super().__gt__(self, other)

    # def __ior__(self, other: set) -> 'RobustSet':
    #     # Override update with union operation
    #     super().__ior__(self, other)
    #     return self

    # def __iand__(self, other: set) -> 'RobustSet':
    #     # Override update with intersection operation
    #     super().__iand__(self, other)
    #     return self

    # def __isub__(self, other: set) -> 'RobustSet':
    #     # Override update with difference operation
    #     super().__isub__(self, other)
    #     return self

    # def __ixor__(self, other: set) -> 'RobustSet':
    #     # Override update with symmetric difference operation
    #     super().__ixor__(self, other)
    #     return self

    def __str__(self):
        # print('__str__()')
        return str(set(self))  # Convert to set for string representation

    def __repr__(self):
        # print('__repr__()')
        return str(set(self))  # Convert to set for representation


s1 = RobustSet({1, 3, 4, 9, 6})
s2 = RobustSet({6, 9, 1, 0})

# print(s1 | s2)
# print(s1 & s2)
# print(s1 - s2)
# print(s1 ^ s2)
# print(s1)
print()
print(f'{s1 = }')
print(f'{s2 = }\n')
# print(s1.remove(6, 3, 8, 10, 3, 3, 1, 8, {}, set(), (), []))

print(s1.replace(1, 3))



# print(s1.pop())
# print(s2 <= s1)
print(f'{s1 = }')
print(f'{s2 = }')

# s1.clear()
# print(s1)
# s1.clear()
# print(s1)