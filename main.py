
def main():
    # print the report header
    print("---Begin report of books/frankenstein.txt ---")

    # print word count in book
    book_string = stringify_book("books/frankenstein.txt")
    words_count = (word_count(book_string))
    print(f"{words_count} words found in the document\n")

    # count letters and print letter count 
    letter_count = (letters_count(book_string))
    for item in letter_count:
        if item.isalpha() and item != ' ':
            print(f"The '{item}' character was found {letter_count[item]} times")

    # print the report footer
    print("---End of report---")

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
    # fill the dictionary with letter counts
    for char in string:
        letter_count[char] = letter_count.get(char, 0) + 1

    # make the dict an array of dicts so it's sortable by value
    letter_list = []
    for letter in letter_count:
        letter_list.append({"letter": letter, "count": letter_count[letter]})

    letter_list.sort(reverse=True, key=sort_dict)
    final_dict = {}
    for dict in letter_list:
        final_dict.update({dict["letter"]: dict["count"]})

    return final_dict


def sort_dict(dict):
    return dict["count"]





main()