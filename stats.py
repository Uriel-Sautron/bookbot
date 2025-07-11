def get_num_words(book_text):
    return len(book_text.split())


def get_num_chars(book_text):
    num_chars = {}
    for char in book_text.lower():
        if char not in num_chars:
            num_chars[char] = 1
        else:
            num_chars[char] += 1
    return num_chars


def sort_dict_by_value(dict):
    new_list = []
    for key, value in sorted(dict.items(), key=lambda item: item[1], reverse=True):
        if key.isalpha():
            new_list.append({"char": key, "num": value})
    return new_list
