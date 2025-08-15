def count_words(text):
    """Return the number of words in the given text."""
    words = text.split()
    return len(words)


def count_characters(text):
    """Return a dictionary mapping each character to its count in the text."""
    char_counts = {}
    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_char_counts(char_dict):
    """Return a sorted list of dictionaries with char and num keys, sorted by count (descending)."""
    char_list = []
    for char, count in char_dict.items():
        if char.isalpha():  # Only include alphabetic characters
            char_list.append({"char": char, "num": count})
    char_list.sort(key=lambda x: x["num"], reverse=True)
    return char_list
