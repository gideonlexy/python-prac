def find_largest_number(arr):
    """ 
    :type arr: List[int] 
    :rtype: int 
    """
    
    largest = arr[0]
   
    for num in arr:
       if num > largest:
           largest = num
    return largest

