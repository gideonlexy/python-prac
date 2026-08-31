def find_max_value(dictionary):
    """ 
    :type dictionary: dict
    :rtype: tuple
    """
    max_number = float('-inf')
    max_key = None
    max_index = None
    for i, (key,val) in enumerate(dictionary.items()):
        if val > max_number:
            max_number = val
            max_key = key
            max_index = i
    return [max_number, max_key, max_index]
        