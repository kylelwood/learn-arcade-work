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

    alice_file = open("AliceInWonderLand200.txt")
    alice_text = []

    for each_line in alice_file:
        alice_text.append(each_line)
        #words = []
        #each_line = split_line(each_line)
        #words.append(each_line)

        #for word in dictionary_list:
           # line_number = 0
            #line_number += 1
            #if not word != dictionary_list:
             #   print("line", line_number, "has misspelled word", word)

    alice_file.close()

    return dictionary_list, alice_file


def linear_search(dictionary_list, word_list):
    print("---Linear Search---")

    list_pos = 0
    while list_pos < len(word_list) and word_list[list_pos] != dictionary_list:
        list_pos += 1

    if list_pos < len(word_list):
        print("the word is not in the list")
    else:
        print("not in list")


def main():
    word_list, dictionary_list = read_in_file("AliceInWonderLand200.txt")
    linear_search(dictionary_list, word_list)


main()
