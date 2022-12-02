"""
This is my Python implementation for the 2022 Advent of Code: Day 1

Puzzle #1:
The jungle must be too overgrown and difficult to navigate in vehicles or access from the air; the Elves' expedition traditionally goes on foot. As your boats approach land, 
the Elves begin taking inventory of their supplies. One important consideration is food - in particular, the number of Calories each Elf is carrying (your puzzle input).

The Elves take turns writing down the number of Calories contained by the various meals, snacks, rations, etc. that they've brought with them, one item per line. Each Elf 
separates their own inventory from the previous Elf's inventory (if any) by a blank line.

For example, suppose the Elves finish writing their items' Calories and end up with the following list:

1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
This list represents the Calories of the food carried by five Elves:

The first Elf is carrying food with 1000, 2000, and 3000 Calories, a total of 6000 Calories.
The second Elf is carrying one food item with 4000 Calories.
The third Elf is carrying food with 5000 and 6000 Calories, a total of 11000 Calories.
The fourth Elf is carrying food with 7000, 8000, and 9000 Calories, a total of 24000 Calories.
The fifth Elf is carrying one food item with 10000 Calories.
In case the Elves get hungry and need extra snacks, they need to know which Elf to ask: they'd like to know how many Calories are being carried by the Elf carrying the 
most Calories. In the example above, this is 24000 (carried by the fourth Elf).

Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
"""

class Elf:
    def __init__(self, calorie_list: list) -> None:
        """
        Initializes an Elf with a calorie count starting at 0.
        """
        self.calories_carried: int = 0
        for calorie_entry in calorie_list:
            self.calories_carried += calorie_entry
        
    def get_calories_carried(self) -> int:
        return self.calories_carried

def get_elves_from_input(input_file_url) -> list[Elf]:
    """
    Compiles a list of elves with calorie count based on the input provided in the input file.
    """
    elves: list[Elf] = []
    calorie_buffer: list[int] = [] # Will store a stream calorie amounts attributed to one elf

    with open(input_file_url, 'r') as input_file:
        for line in input_file.readlines():
            if line.isspace():
                # Empty line means to empty calorie buffer into a new Elf and add it to the elves collection
                elves.append(Elf(calorie_buffer))
                calorie_buffer = [] # Empty buffer
            else:
                # Add number to buffer
                calorie_buffer.append(int(line))

        if len(calorie_buffer) > 0:
            elves.append(Elf(calorie_buffer))

    return elves

def get_elves_in_caloric_order(elves: list[Elf]) -> list[Elf]:
    """
    Sorts a list of Elf objects by calorie count in descending order and returns the list.
    """
    elves.sort(key = lambda elf: elf.get_calories_carried(), reverse=True)
    return elves

def day_one_puzzle_one(elves: list[Elf]) -> None:
    """
    Implementation for the 1st puzzle of day 1. Reads in input and addresses the above problem.
    """
    print(elves[0].get_calories_carried())

"""
Puzzle #2:
--- Part Two ---
By the time you calculate the answer to the Elves' question, they've already realized that the Elf carrying the most Calories of food might eventually run 
out of snacks.

To avoid this unacceptable situation, the Elves would instead like to know the total Calories carried by the top three Elves carrying the most Calories. 
That way, even if one of those Elves runs out of snacks, they still have two backups.

In the example above, the top three Elves are the fourth Elf (with 24000 Calories), then the third Elf (with 11000 Calories), then the fifth Elf (with 
10000 Calories). The sum of the Calories carried by these three elves is 45000.

Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
"""

def day_one_puzzle_two(elves: list[Elf]) -> None:
    """
    Implementation for the 2nd puzzle of day 1. Reads in input and addresses the above problem.
    """
    print(sum([elf.get_calories_carried() for elf in elves[:3]]))

if __name__ == "__main__":
    input_file_url: str = "../input/day_one_puzzle_one_input.txt"
    elves_from_input: list[Elf] = get_elves_from_input(input_file_url)

    # Sort in descending order by # calories
    elves = get_elves_in_caloric_order(elves_from_input) 

    day_one_puzzle_one(elves)
    day_one_puzzle_two(elves)