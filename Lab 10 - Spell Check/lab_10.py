import re


def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


def read_in_file(file_name):

    dictionary_file = open("dictionary.txt")

    dictionary_list = []

    for line in dictionary_file:
        line = line.strip()

        dictionary_list.append(line)

    dictionary_file.close()

    print("---Linear Search---")

    alice_file = open("AliceInWonderLand200.txt")

    for each_line in alice_file:
        words = []
        each_line = split_line(each_line)
        words.append(each_line)

        for word in dictionary_list:
            line_number = 0
            line_number += 1
            if not word != dictionary_list:
                print("line", line_number, "has misspelled word", word)

    alice_file.close()

    return dictionary_list


def linear_search(key, word_list):
    list_pos = 0

    while list_pos < len(word_list) and word_list[list_pos] != key:
        list_pos += 1

    if list_pos < len(word_list):
        print("word found at position", list_pos)
    else:
        print("not found")
    return list_pos


def main():
    key = "Alice in Wonderland"

    word_list = read_in_file("AliceInWonderLand200.txt")
    linear_search(key, word_list)


main()
