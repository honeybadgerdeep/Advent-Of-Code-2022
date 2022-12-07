def characters_are_unique(string: str) -> bool:
    """
    Determines whether the characters are unique within the given string.
    """
    encountered = {}
    # Parse until there's a duplicate character found
    for c in string:
        if c in encountered:
            return False
        else:
            encountered[c] = True

    # If the whole string is parsable, then it has distinct characters
    return True


def determine_characters_to_marker(lines: list[str], marker_length: int) -> int:
    """
    Determines the number of characters that need to be processed before the
    marker is detected. The marker is a string of all distinct characters 
    of length (marker_length)
    """
    buffer = ""
    line_idx = 0
    characters_processed = marker_length - 1 # From start of buffer
    for line in lines:
        char_idx = 0
        for c in line:

            # possible to make buffer of length-marker_length in this line
            if (char_idx < len(line) - (marker_length - 1)):
                buffer = line[char_idx:char_idx + marker_length]

            # possible to use an additional line to build length-marker_length buffer
            elif (line_idx < len(lines) - 1 and len(lines[line]) >= (marker_length - 1)): 
                # Whatever is left of the current line
                buffer = line[char_idx:]

                # Determine amt needed to make marker_length
                len_remainder = marker_length - len(buffer)

                # Add that many characters to the buffer to complete it
                buffer += lines[line_idx + 1][:len_remainder]
            
            characters_processed += 1
            char_idx += 1

            if (characters_are_unique(buffer)):
                return characters_processed

        line_idx += 1


def day_six_puzzle_one(input: str):
    """
    Determine the number of characters that need to be processed before the 
    start-of-packet marker is detected.
    """

    with open(input, 'r') as file:
        lines = file.readlines()
        return determine_characters_to_marker(lines, 4)

def day_six_puzzle_two(input: str):
    """
    Determine the number of characters that need to be processed before the
    start-of-message marker is detected.
    """

    with open(input, 'r') as file:
        lines = file.readlines()
        return determine_characters_to_marker(lines, 14)

from test import test_outcome

if __name__ == "__main__":
    expected_values_one = [7, 5, 6, 10, 11]

    # Test inputs for puzzle #1 - ALL PASS!
    for i in range(len(expected_values_one)):
        test_name = "Day 6: Puzzle 1, Test #{num}".format(num = i + 1)
        test_input = "../input/day_six_puzzle_one_test_{num}.txt".format(num = i + 1)
        test_outcome(test_name, day_six_puzzle_one(test_input), expected_values_one[i])

    input = "../input/day_six_puzzle_one_input.txt"
    print(day_six_puzzle_one(input))

    expected_values_two = [19, 23, 23, 29, 26]
    # Test inputs for puzzle #2 
    for i in range(len(expected_values_two)):
        test_name = "Day 6: Puzzle 2, Test #{num}".format(num = i + 1)
        test_input = "../input/day_six_puzzle_one_test_{num}.txt".format(num = i + 1)
        test_outcome(test_name, day_six_puzzle_two(test_input), expected_values_two[i])

    input = "../input/day_six_puzzle_one_input.txt"
    print(day_six_puzzle_two(input))