from stats import word_counter, char_counter, sort_dictionary

def get_book_text(filepath):
    ret_string = ""
    with open(filepath) as file:
        ret_string = file.read()
    return ret_string

def main():
    frankenstein_text = get_book_text("./books/frankenstein.txt")
    word_count = word_counter(frankenstein_text)
    print(f"{word_count} words found in the document")
    char_count = char_counter(frankenstein_text)
    # for key in char_count:
    #     print(f"'{key}': {char_count[key]}")
    list_dict = sort_dictionary(char_count)
    print(list_dict)

main()