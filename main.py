
def count_letters(string, file_contents):
    letter_count_dict = {}
    lower_case_string = string.lower()
    for char in lower_case_string:
        if not char.isalpha():
            raise ValueError(f"Incorrect input: {char} in {string} is not a letter")
        else:
            letter_count_dict[char] = 0
            for word in file_contents.split():
                for char in word:
                    lowercase_char = char.lower()
                    if lowercase_char in letter_count_dict:
                        letter_count_dict[lowercase_char] += 1

    return letter_count_dict

with open("./books/frankenstein.txt") as f:
    file_contents = f.read()
    words = file_contents.split()
    try:
        letter_count_dict = count_letters("abcdefghijklmnopqrstuvwxyz", file_contents)
    except Exception as e:
        print(e)
    else:
        letter_count_letter_list = list(letter_count_dict.keys())
        letter_count_letter_list.sort()
        print("--- Begin report of ./books/frankenstein.text ---")
        print(f"{len(words)} word found in the document")
        print()
        for letter in letter_count_letter_list:
            print(f"The '{letter}' character was found {letter_count_dict[letter]} times")
        print("--- End report ---")
