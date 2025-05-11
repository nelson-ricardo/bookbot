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
    list_dict = unsorted_dict.items()
    return list_dict