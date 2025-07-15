import sys
from stats import get_book_text, get_wordcount, get_lettercount, sorted_dictionary

def main():
    try:
        source = sys.argv[1]
        text = get_book_text(source)
        num_words = get_wordcount(text)
        num_chars = get_lettercount(text)
        sorted_chars = sorted_dictionary(num_chars)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {source}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for entry in sorted_chars:
            if entry['char'].isalpha():
                print(f"{entry['char']}: {entry['num']}")
        print("============= END ===============")
        return None
    except IndexError:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
main()