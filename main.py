
def main():
    # print_book("books/frankenstein.txt")   
    print("---Begin report of books/frankenstein.txt ---")

    
    book_string = stringify_book("books/frankenstein.txt")
    words_count = (word_count(book_string))
    print(f"{words_count} words found in the document")

    letter_count = (letters_count(book_string))
    for item in letter_count:
        print(f"The {item} character was found {letter_count[item]} times")

def print_book(book_url):
    
    with open(book_url) as book_text:
        print(book_text.read())

def stringify_book(book_url):
    with open(book_url) as book_text:
        return book_text.read()
    
def word_count(string):
    return len(string.split())

def letters_count(string):
    string = string.lower()
    letter_count = {}
    for char in string:
        letter_count[char] = letter_count.get(char, 0) + 1

    return letter_count


main()