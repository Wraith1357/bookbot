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



def sort_list_dict(char_count):

    """
    char_keys = list(char_count.keys())
    #print(char_keys) prints keys confirmed
    alpha_char_keys = []

    for char in char_keys:
        if(char.isalpha()):
            alpha_char_keys.append(char)

    print(alpha_char_keys)
    I did this first, but realized it weasn't really the right way to do what i wanted to do
    """


    alpha_dict = {}
    for char in char_count:
        if (char.isalpha()):
            alpha_dict[char] = char_count[char]

    #print(alpha_dict)


    #now I need to make a sorted list of dictionaries, with each dictionary having 2 key value pairs
    # the pairs should look something like this {"char": "b", "num": 2300}
    list_dicts = []
    for char in alpha_dict:
        list_dicts.append({"char": char, "num": alpha_dict[char]})
    #print("line breaker")
    #print(list_dicts)

    list_dicts.sort(reverse = True, key = sort_by_this)
    #print("line breaker") 
    #print("line breaker")
    #print(list_dicts)
    
    #this is now sorting the list of dictionaries correctly, now I need to return the sorted list
    #   instead of printing it directly from the function, and then format the print properly within
    #   main
    return list_dicts
    """
    for char in char_keys:
        if(char.isalpha() != True):
            char_keys.remove(char)      Not really sure what i did wrong here, might be retarded right now
    print(char_keys)                    but oh well. the first for loop only got rid of a few chars that
    for char in char_keys:              needed to be removed from the list, but not even most of them.
        if(char.isalpha() != True):     so, I just redid the same for loop multiple mtimes and eventually 
            char_keys.remove(char)      there were enough loops that it got rid of everything that should
    print(char_keys)                    have been removed, but that looks dumb and I know it shouldn't be
    for char in char_keys:              working like that, so I just decided making a new list would be
        if(char.isalpha() != True):     easier than figuring out what was wrong, and it was.
            char_keys.remove(char)
    print(char_keys)
    for char in char_keys:
        if(char.isalpha() != True):
            char_keys.remove(char)
    print(char_keys)
    for char in char_keys:
        if(char.isalpha() != True):
            char_keys.remove(char)
    print(char_keys)
    """

def sort_by_this(items):
    return items["num"]

