"""Splits a list into at most n groups, with leftovers in the last group."""


def groupArrayElements(items:list,n:int):
    """Splits a list into at most n equal-sized groups, with any remainder in the last group,
    which may be smaller.
    
    Returns [] for an empty list. Raises TypeError/ValueError for invalid input."""

    if not isinstance(items, list): # Check that items is actually a list
        raise TypeError("items must be a list") 
    
    # Check n is an int (bool is subclass of int)
    if not isinstance(n, int) or isinstance(n, bool): 
        raise TypeError("n must be an integer") 
    
    if n < 1: # Check that n is at least 1 
        raise ValueError("n must be 1 or greater") 
    
    if not items: # Checks for empty list
        return []  

    # Round up, so the leftover items fit without an extra group.
    groupSize = len(items)//n # Using DIV to get the group size rounded down
    if len(items) % n != 0: # Using MOD to check for remainder
        groupSize += 1 # If there is a remainder, add 1 to round up the group size

    groups = []
    for start in range(0, len(items), groupSize): # Loop through the list, increment by group size each time
        end = start + groupSize # Work out where the current group ends
        groups.append(items[start:end]) # Take items from start up to element before end and add them as a new group
    return groups 


#Test runs to check functionality
def _raises(exc,*args):
    try:
        groupArrayElements(*args)
    except exc:
        return True
    return False


if __name__ == "__main__":
    assert groupArrayElements([1, 2, 3, 4, 5], 3) == [[1, 2], [3, 4], [5]]
    assert groupArrayElements([1, 2, 3, 4, 5, 6], 3) == [[1, 2], [3, 4], [5, 6]]
    assert groupArrayElements([], 3) == []
    assert groupArrayElements([1, 2, 3], 1) == [[1, 2, 3]]
    assert groupArrayElements([1, 2], 5) == [[1], [2]]
    assert groupArrayElements([[1],[3,2],[1],[[4,5],2]],3) == [[[1],[3,2]],[[1],[[4,5],2]]]
    # rounding up can give fewer than n groups
    assert groupArrayElements([1, 2, 3, 4, 5], 4) == [[1, 2], [3, 4], [5]]

    original = [1, 2, 3, 4, 5]
    groupArrayElements(original, 3)
    assert original == [1, 2, 3, 4, 5]

    for badN in (0, -2):
        assert _raises(ValueError, [1, 2, 3], badN), badN
    for badN in (2.5, "3", True):
        assert _raises(TypeError, [1, 2, 3], badN), badN
    assert _raises(TypeError, "not a list", 2)

    print("All checks passed.")
