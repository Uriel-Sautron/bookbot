from stats import get_num_words, get_num_chars, sort_dict_by_value
import sys

def get_book_text(book_path):
    with open(book_path) as book:
        return book.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    num_chars = get_num_chars(book_text)
    num_chars_sorted = sort_dict_by_value(num_chars)
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print(f"----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print(f"----------- Character Count ----------")
    for char in num_chars_sorted:
        print(f"{char['char']}: {char['num']}")
    print(f"============= END ===============")

main()
