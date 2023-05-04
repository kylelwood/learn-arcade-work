def read_in_file(file_name):
    """ Read in lines from a file """

    # Open the file for reading, and store a pointer to it in the new
    # variable "file"

    dictionary_file = open("dictionary.txt")

    dictionary_list = []

    for line in dictionary_file:
        line = line.strip()

        dictionary_list.append(line.upper())

    dictionary_file.close()

    alice_file = open(file_name)

    # Create an empty list to store our names
    word_list = []

    # Loop through each line in the file like a list
    for line in alice_file:
        # Remove any line feed, carriage returns or spaces at the end of the line
        line = line.strip()

        # Add the name to the list
        word_list.append(line)

    alice_file.close()

    return word_list


def linear_search(key, word_list):
    """ Linear search """

    # Start at the beginning of the list
    current_list_position = 0

    # Loop until you reach the end of the list, or the value at the
    # current position is equal to the key
    while current_list_position < len(word_list) and word_list[current_list_position] != key:

        # Advance to the next item in the list
        current_list_position += 1

    return current_list_position


def main():

    key = "Alice in Wonderland"
    name_list = read_in_file("AliceInWonderLand200.txt")
    list_position = linear_search(key, name_list)

    if list_position < len(name_list):
        print("The word", key, "is at position", list_position)
    else:
        print("The word", key, "was not in the list.")


main()
