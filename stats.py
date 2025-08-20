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



def character_count(text_string):
    char_dict = {}
    
    lower_text_string = text_string.lower()
    #print(lower_text_string) --Test, did work, all letters are lowercase
    """
    for char in lower_text_string:
        print(f"{char} = 1")
        test to make sure I did this right
    """
    for character in lower_text_string:
        if character in char_dict:
            char_dict[character] += 1
        else:
            char_dict[character] = 1

    return char_dict


