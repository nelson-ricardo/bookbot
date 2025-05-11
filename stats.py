# function used in sort_dictionary
def key_func(e):
    return e[1]

def word_counter(text):
    word_count = len(text.split())
    return word_count

def char_counter(text):
    ret_dict = {}

    for char in text:
        lowered_char = char.lower()
        if lowered_char in ret_dict:
            ret_dict[lowered_char] += 1
        else:
            ret_dict[lowered_char] = 1
    
    return ret_dict

def sort_dictionary(unsorted_dict):
    list_dict = list(unsorted_dict.items())
    # sort by the the number of times an item appears in the list
    list_dict.sort(reverse=True, key=key_func)
    
    # create a list of dictionary
    ret_list = []
    for item in list_dict:
        ret_list.append({item[0]:item[1]})
    
    return ret_list