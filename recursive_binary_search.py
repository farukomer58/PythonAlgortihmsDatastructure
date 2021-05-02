def recursive_binary_search(list, target):
    """
    Returns the index position of the target if found, else returns None with Recursion
    NOTE list has to be SORTED
    """
    if(len(list) == 0):
        return False
    else:
        midpoint=(len(list))//2
        if list[midpoint] == target:
            return True
        else:   
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint+1:],target)
            else:
                return recursive_binary_search(list[:midpoint],target)

def verify(result):
    print("Target found: ", result)

numbers=[1,2,3,4,5,6,7,8,9,10]

searchResult = recursive_binary_search(numbers,1)
verify(searchResult)

searchResult2 = recursive_binary_search(numbers,12)
verify(searchResult2)