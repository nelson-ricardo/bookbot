from stats import word_counter, char_counter, sort_dictionary

def get_book_text(filepath):
    ret_string = ""
    with open(filepath) as file:
        ret_string = file.read()
    return ret_string

def main():
    filepath = "books/frankenstein.txt"

    frankenstein_text = get_book_text(filepath)
    char_count = char_counter(frankenstein_text)
    
    # list of dictionarys {char: num_of_times}
    list_dict = sort_dictionary(char_count)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    word_count = word_counter(frankenstein_text)
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    # TODO: debug this!
    for dictionary in list_dict:
        key = list(dictionary.keys())[0]
        if key.isalpha():
            print(f"{key}: {dictionary[key]}")
    print("============= END ===============")

main()