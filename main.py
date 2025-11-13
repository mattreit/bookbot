import sys
from stats import get_num_words, get_char_stats, sort_dict

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    num_words = get_num_words(book_text)
    char_dict = get_char_stats(book_text)
    sorted_list = sort_dict(char_dict)

    print("=========== BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for i in sorted_list:
        print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")
    
def get_book_text(file_path):
    with open(file_path) as f:
        book_text = f.read()
    return book_text

main()
