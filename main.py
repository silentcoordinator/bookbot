from stats import get_word_count
from stats import getCharacterCount
from stats import sorting_dict
import sys

def get_book_text(book):
    try:
        with open(book) as f:
            fileContent = f.read()
            return fileContent
    except Exception as e:
        print(e)

def main():
    if len(sys.argv) == 2:
        book = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    bookString = get_book_text(book)
    words = get_word_count(bookString)
    character_count = getCharacterCount(bookString)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")


    listSorted = sorting_dict(getCharacterCount(bookString))
    for i in listSorted:
        for key,value in i.items():
            print(f"{key}: {value}")

    print("============= END ===============")

main()
