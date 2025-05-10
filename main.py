def get_book_text(filepath):
    ret_string = ""
    with open(filepath) as file:
        ret_string = file.read()
    return ret_string

def main():
    frankenstein_text = get_book_text("./books/frankenstein.txt")
    print(frankenstein_text)

main()