def get_num_words(book_text):
    return len(book_text.split())

def get_char_stats(book_text):
    char_dict = {}
    book_text = book_text.lower()
    for char in book_text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict 

def sort_dict(dict):
    dict_list = []
    for i in dict:
        if i.isalpha():
            temp_dict = {"char": i, "num": dict[i]}
            dict_list.append(temp_dict)

    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

def sort_on(dict):
    return dict["num"]
