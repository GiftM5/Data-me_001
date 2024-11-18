# TODO: Implement the following functions based on the descriptions.

def reverse_list(lst):
    
    """
    Reverses the given list.
    :param lst: List of integers.
    :return: A list with elements in reverse order.
    """
    pass  # Implement this
    new_list = lst[::-1]
    return new_list
print(reverse_list([1, 2, 3]))

        
    


def count_occurrences(lst, element):
    """
    Counts how many times the given element appears in the list.
    :param lst: List of elements.
    :param element: Element to count.
    :return: Integer count of occurrences.
    """
    pass  # Implement this
    element_count = 0
    for element in lst:
        if lst[element] == lst[element] :
            element_count +=1
            return element_count
        else:
            return "There are no repeating elements"
print(count_occurrences([1, 2, 2, 3],2))

def get_keys_with_value(dct, value):
    """
    Returns a list of keys that have the given value in the dictionary.
    :param dct: Dictionary to search.
    :param value: Value to find.
    :return: List of keys.
    """
    pass  # Implement this

def merge_sorted_lists(lst1, lst2):
    """
    Merges two sorted lists into one sorted list.
    :param lst1: First sorted list.
    :param lst2: Second sorted list.
    :return: Merged sorted list.
    """
    pass  # Implement this
    Total_lists = lst1 + lst2
    return sorted(Total_lists)
print(merge_sorted_lists([1, 3, 5],[2, 4, 6]))

def find_second_largest(numbers):
    """
    Finds the second largest number in a list.
    :param numbers: List of integers.
    :return: The second largest integer.
    """
    pass  # Implement this


def is_anagram(str1, str2):
    """
    Checks if two strings are anagrams.
    
    An anagram is a word or phrase formed by rearranging the letters of another,
    using all the original letters exactly once. For example, "listen" and "silent"
    are anagrams because they use the same letters in a different order.
    
    :param str1: First string.
    :param str2: Second string.
    :return: True if the strings are anagrams, False otherwise.
    """
    pass  # Implement this
    # for words in str1:
    #     if str1[1::] ==


def flatten_list(nested_list):
    """
    Flattens a nested list into a single list.
    :param nested_list: List of lists.
    :return: A flat list with all elements.
    """
    pass  # Implement this


def remove_duplicates(lst):
    """
    Removes duplicates from the list while maintaining order.
    :param lst: List of elements.
    :return: List without duplicates.
    """
    pass  # Implement this
   
    new_list = []
    for element in lst:
        if lst[element] != lst[element]:
            new_list = new_list.append(lst(element))
            return new_list
        else:
            return lst

print(remove_duplicates([1,2,2,3]))

def find_common_elements(lst1, lst2):
    """
    Finds common elements between two lists.
    :param lst1: First list.
    :param lst2: Second list.
    :return: List of common elements.
    """
    pass  # Implement this