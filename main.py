
def main():

    with open("books/frankenstein.txt", "r") as f:
        content = f.read()
        word_count = sum(len(line.split()) for line in content.splitlines())
        char_counts = count_chars(content)

def count_chars(book):
    char_counts = {}
    char_count = 0
    lowercase_book = book.lower()

    for char in lowercase_book:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

if __name__ == "__main__":
    main()
