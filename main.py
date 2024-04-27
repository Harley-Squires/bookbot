def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars = get_num_chars(text)
    print(f"{num_words} words found in the document")
    print(f"{num_chars} is the char dictionary!")


def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_chars(text):
    chars_dict = {}
    for l in text:
        lowered = l.lower()
        if lowered in chars_dict:
            chars_dict[lowered] += 1
        else:
            chars_dict[lowered] = 1
    return chars_dict

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
