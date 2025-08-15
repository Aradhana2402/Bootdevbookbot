import sys
from stats import count_words, count_characters, sort_char_counts

def get_book_text(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def main():
    # Ensure correct usage
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    book_text = get_book_text(path)

    # Word & character counts
    num_words = count_words(book_text)
    char_counts = count_characters(book_text)
    sorted_chars = sort_char_counts(char_counts)

    # Report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()
