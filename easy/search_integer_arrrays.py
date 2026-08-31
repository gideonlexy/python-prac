# Return : a list cointaining maximum subarray sum, the start index and the end index of the subarray
# Example : [-2, 1, -3, 4, -1, 2, 1, -5, 4] - > [6, 3, 6]

def max_subarray_sum(arr):
    """ 
    :type input: List[int]
    :rtype: List[int] 
    """

 
    current_sum = arr[0]
    best_sum = arr[0]
    
    current_start = 0
    best_start = 0
    best_end = 0
    
    
    for i in range(1, len(arr)):
        # Should we start a new subarray here?
        if arr[i] > current_sum + arr[i]:
            current_sum = arr[i]
            current_start = i

        # Or continue the existing subarray?    
        else:
            current_sum += arr[i]
        # Did we find a new best?
        if current_sum > best_sum:
            best_sum = current_sum
            best_start = current_start
            best_end = i
        
    return [best_sum, best_start, best_end]
        
        
    