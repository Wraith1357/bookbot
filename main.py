from stats import find_num_words
from stats import character_count


def get_book_text(file_path):

    with open(file_path) as f:
        file_contents = f.read()
    
    return file_contents



def main():
    text_contents = get_book_text("books/frankenstein.txt")

    print(f"{find_num_words(text_contents)} words found in the document")
    
    char_count = character_count(text_contents)
    print(char_count)



main()