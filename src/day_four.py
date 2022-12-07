def get_range_from_input(input: str):
    tokens = input.split('-')
    return [int(tokens[0]), int(tokens[1])]

def range_containment(range1, range2):
    return (range1[0] <= range2[0] and range1[1] >= range2[1]) or (range1[0] >= range2[0] and range1[1] <= range2[1])

def day_four_puzzle_one(input_file_url: str):
    contains_ct = []
    with open(input_file_url, 'r') as file:
        for line in file.readlines():
            tokens = line.split(',')
            range1 = get_range_from_input(tokens[0])
            range2 = get_range_from_input(tokens[1])
            if (range_containment(range1, range2)):
                contains_ct.append(1)

    print(sum(contains_ct))

def within_range(num, num_range):
    return num <= num_range[1] and num >= num_range[0]

def ranges_overlap(range1, range2):
    return within_range(range1[0], range2) or within_range(range1[1], range2) or within_range(range2[0], range1) or within_range(range2[1], range1)

def day_four_puzzle_two(input_file_url: str):
    overlap_ct = []
    with open(input_file_url, 'r') as file:
        for line in file.readlines():
            tokens = line.split(',')
            range1 = get_range_from_input(tokens[0])
            range2 = get_range_from_input(tokens[1])
            if (ranges_overlap(range1, range2)):
                overlap_ct.append(1)
    
    print(sum(overlap_ct))

if __name__ == "__main__":
    input_file_url: str = "../input/day_four_puzzle_one.txt"
    day_four_puzzle_one(input_file_url)
    day_four_puzzle_two(input_file_url)