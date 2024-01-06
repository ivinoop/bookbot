def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"There are {num_words} words in the book")
    num_letters = get_letters(text)
    print(num_letters)


def get_letters(text):
    letters = {}
    for letter in text:
        lowercase = letter.lower()
        if lowercase in letters:
            letters[lowercase] += 1
        else:
            letters[lowercase] = 1
    return letters


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()