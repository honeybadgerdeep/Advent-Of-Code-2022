def get_common_character(strings) -> str:
    """
    Gets the common character between strings in a list.
    """
    freq = {} # Character frequency tracker

    idx = 0
    # Update character frequency across all strings
    for string in strings:
        for c in string:
            if c not in freq:
                freq[c] = {}
                freq[c][idx] = True
            else:
                if (idx not in freq[c]):
                    freq[c][idx] = True
                if (len(freq[c].keys()) == len(strings)):
                    return c    
        idx += 1
    


    # Return empty string by default
    return ''

def in_between_range(num: int, lower: int, upper: int) -> bool:
    return num >= lower and num <= upper

def character_to_priority(chr: str) -> int:
    ascii_val = ord(chr)
    if in_between_range(ascii_val, ord('a'), ord('z')):
        return ascii_val - 96
    elif in_between_range(ascii_val, ord('A'), ord('Z')):
        return ascii_val - 38
    return -1

def get_rucksack_types_from_input(input_file_url: str):
    rucksack_priorities = []

    with open(input_file_url, 'r') as file:
        for line in file.readlines():
            first_half = line[0:len(line)//2]
            second_half = line[len(line)//2:len(line)]
            common = get_common_character([first_half, second_half])
            if common != '':
                rucksack_priorities.append(character_to_priority(common))

    return rucksack_priorities



def get_badge_types_from_input(input_file_url: str):
    elf_badges = []

    with open (input_file_url, 'r') as file:
        line_ct = 0
        line_buffer = []
        for line in file.readlines():
            line_ct += 1
            line_buffer.append(line)
            if (line_ct % 3 == 0):
                common = get_common_character(line_buffer)
                elf_badges.append(character_to_priority(common))
                line_buffer = []

    return elf_badges

def day_three_puzzle_one(input_file_url: str):
    rucksack_types = get_rucksack_types_from_input(input_file_url)
    print(sum(rucksack_types))

def day_three_puzzle_two(input_file_url: str):
    badge_types = get_badge_types_from_input(input_file_url)
    print(sum(badge_types))

if __name__ == "__main__":
    input_file_url: str = "../input/day_three_puzzle_one.txt"
    day_three_puzzle_one(input_file_url)
    day_three_puzzle_two(input_file_url)