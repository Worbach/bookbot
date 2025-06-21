from stats import get_num_words, get_chars_dict, sort_dic
import sys


def main():
    print("============ BOOKBOT ============")
    # book_path = "books/frankenstein.txt"
    args = sys.argv
    if len(args) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = args[1]
    print(f"Analyzing book found at {book_path}...")
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    report_list = sort_dic(chars_dict)
    print("--------- Character Count -------")
    for element in report_list:
        if element["char"].isalpha():
            print(f"{element["char"]}: {element["num"]}")
    print("============= END ===============")


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()