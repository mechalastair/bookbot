def get_book_text(filepath):
    with open(filepath) as file:
        file_text = file.read()
    return file_text

def get_wordcount(file_text):
    words = len(file_text.split())
    return words

def get_lettercount(file_text):
    chars = {}
    for char in list(file_text.lower()):
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def sort_on(items):
    return items["num"]

def sorted_dictionary(chars):
    char_list = []
    for key, value in chars.items():
        char_dict = {'char': key, 'num': value}
        char_list.append(char_dict)
    char_list.sort(reverse=True, key=sort_on)
    return char_list