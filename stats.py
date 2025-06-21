def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(items):
    return items["num"]


def sort_dic(dic_of_character_and_counts):
    list_of_dic = []
    for char in dic_of_character_and_counts:
        sorted_list_dic = {}
        sorted_list_dic["char"] = char 
        sorted_list_dic["num"] = dic_of_character_and_counts[char]
        list_of_dic.append(sorted_list_dic)
    list_of_dic.sort(reverse=True, key=sort_on)
    return list_of_dic