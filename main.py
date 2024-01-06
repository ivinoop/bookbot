def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    # print(f"There are {num_words} words in the book")
    num_letters = get_letters(text)
    # print(num_letters)
    report_list = dict_to_list(num_letters)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in report_list:
        if not item["letter"].isalpha():
            continue
        print(f"The '{item['letter']}' character was found {item['count']} times")

    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_num_words(text):
    words = text.split()
    return len(words)


def get_letters(text):
    letters = {}
    for letter in text:
        lowercase = letter.lower()
        if lowercase in letters:
            letters[lowercase] += 1
        else:
            letters[lowercase] = 1
    return letters


def dict_key(book_dict):
  return book_dict["count"]


def dict_to_list(book_dict):
  report_list =[]
  for i in book_dict:
    report_list.append({"letter": i, "count": book_dict[i]})
  report_list.sort(reverse=True, key=dict_key)
  return report_list







main()