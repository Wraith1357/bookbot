
def get_book_text(file_path):

    with open(file_path) as f:
        file_contents = f.read()
    
    return file_contents



def find_num_words(text_contents):
    words_list = []
    words_list.extend(text_contents.split())
    #print(words_list) test stuff
    num_words = len(words_list)
    #print(num_words)
    return num_words
"""
took a little while for me to figure out why this was only giving me a 1 as the number of words.
turns out, append only adds one item at a time, so i was adding the entire list made by split as 
a single item. Make sure I know how these functions work before using them lol
"""



def main():
    text_contents = get_book_text("books/frankenstein.txt")

    print(f"{find_num_words(text_contents)} words found in the document")
    



main()