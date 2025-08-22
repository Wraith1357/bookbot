from stats import find_num_words
from stats import character_count
from stats import sort_list_dict

def get_book_text(file_path):

    with open(file_path) as f:
        file_contents = f.read()
    
    return file_contents



def main():
    text_contents = get_book_text("books/frankenstein.txt")

    #print(f"{find_num_words(text_contents)} words found in the document")
    
    char_count = character_count(text_contents)
    #print(char_count)

    sorted_list = sort_list_dict(char_count)
    #print(sorted_list)  #because I now have the full sorted list, I can stop using the previous test
                        #   and start just making the format print
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {find_num_words(text_contents)} total words")
    print("--------- Character Count -------")
    for element in sorted_list:
        print(f"{element["char"]}: {element["num"]}")
    print("============= END ===============")



main()