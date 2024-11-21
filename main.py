def main():

    file_path        = "books/frankenstein.txt"
    text             = get_book_text(file_path)
    word_count       = get_word_count(text)
    char_dict        = get_char_dict(text)
    sorted_char_dict = char_dict_list(char_dict)

    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the file")
    print()

    for letter in sorted_char_dict:
        if not letter["char"].isalpha():
            continue
        print(f"The '{letter['char']}' character was found {letter['num']} times")

    print("--- END REPORT ---")

# ----------------------------------------
# 
# ----------------------------------------
def sort_on(value):
    return value["num"]

# ----------------------------------------
# LIST SORTING FUNCTION
# ----------------------------------------
def char_dict_list(dictionary):
    sorted_list = []
    for ch in dictionary:
        sorted_list.append({"char": ch, "num": dictionary[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

# ----------------------------------------
# CREATE/ADD TO CHAR. DICTIONARY FUNCTION
# ----------------------------------------
def get_char_dict(text):
    char_dict = {}
    for char in text:
        lower_char = char.lower()
        if lower_char in char_dict:
            char_dict[lower_char] += 1
        else:
            char_dict[lower_char] = 1
    # print(f"{char_dict}")
    return char_dict

# ----------------------------------------
# GET WORD COUNT FUNCTION
# ----------------------------------------
def get_word_count(text):
    words = text.split()
    return len(words)

# ----------------------------------------
# READ FILE FUNCTION
# ----------------------------------------
def get_book_text(file_path):

    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

main()