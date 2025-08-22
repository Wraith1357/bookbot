import sys
from stats import find_num_words
from stats import character_count
from stats import sort_list_dict


def get_book_text(file_path):
    try:
        with open(file_path) as f:
            file_contents = f.read()

    except FileNotFoundError:
        print(f"file <{file_path}> not found")
        sys.exit(1)

    return file_contents



def main():
    #this needs to go from hard-coded to a user input, so all hard-coded filepaths will be changed
    #text_contents = get_book_text("books/frankenstein.txt")
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        #"Improper command, Usage: python3 main.py <file_path>" apparently this line was tracked
        #in the cli, big gay, cause I think my wording is more helpful
    book_path = sys.argv[1]
    #print(book_path)
    text_contents = get_book_text(book_path)

    #print(f"{find_num_words(text_contents)} words found in the document")
    
    char_count = character_count(text_contents)
    #print(char_count)

    sorted_list = sort_list_dict(char_count)
    #print(sorted_list)  #because I now have the full sorted list, I can stop using the previous test
                        #   and start just making the format print
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")#remember to change this from hardcode-done
    print("----------- Word Count ----------")
    print(f"Found {find_num_words(text_contents)} total words")
    print("--------- Character Count -------")
    for element in sorted_list:
        print(f"{element["char"]}: {element["num"]}")
    print("============= END ===============")



main()