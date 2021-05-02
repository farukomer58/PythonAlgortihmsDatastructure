def binary_search(list, target):
    """
    Returns the index position of the target if found, else returns None
    NOTE list has to be SORTED
    """

    first = 0
    last = len(list)-1

    while first<=last:

        midpoint = (first+last)//2 # double slash is a 'floor'division so it rounds down
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:   
            last = midpoint

    return None

def verify(index):
    if index is not None:
        print("Target found at index:", index)
    else:   
        print("Target NOT found in list")

numbers=[1,2,3,4,5,6,7,8,9,10]

searchIndex = binary_search(numbers,10)
verify(searchIndex)