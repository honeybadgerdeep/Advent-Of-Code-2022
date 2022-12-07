"""
This is an implementation of Advent-Of-Code: 2022, Day 5 Puzzle Sets
"""

class Stack:
    """
    Implementation of the stack data structure, using a list.
    """
    def __init__(self) -> None:
        self.contents: list[str] = []
        self.size: int = 0
    
    def pop(self) -> str:
        if (self.size == 0): raise IndexError("Stack is empty!")
        self.size -= 1
        return self.contents.pop()

    def peek(self) -> str:
        if (self.size == 0): raise IndexError("Stack is empty!")
        return self.contents[self.size - 1]
    
    def push(self, val: str) -> str:
        self.size += 1
        self.contents.append(val)

    def get_size(self) -> int:
        return self.size

    def print_stack(self) -> None:
        print(self.contents)

class Instruction:
    """
    Re-formats instructions for easier processing later on.
    """
    def __init__(self, instruction_line: str) -> None:
        """
        Format of instruction_line is: move # from # to #
        """

        # Tokenize into [move, #, from, #, to, #].
        tokens = instruction_line.split()
        self.num_crates = int(tokens[1]) # Move: num_crates
        self.src = int(tokens[3]) # From: src
        self.dest = int(tokens[5]) # To: dest
    
    def get_num_crates(self) -> int:
        return self.num_crates
    
    def get_src(self) -> int:
        return self.src

    def get_dest(self) -> int:
        return self.dest

def idx_to_stack_num(idx: int) -> int:
    """
    Maps the index of a crate character to a corresponding stack no.
    """
    return (idx + 3) // 4

def is_crate(c: str) -> bool:
    """
    Determines whether a given character is a crate character or not.
    """
    if (len(c) != 1): raise Exception("The input should be only a single character!")
    return c != '[' and c != ']' and not c.isspace()

def generate_stack_layout(layout_input: list[str]) -> dict:
    """
    Processes layout lines from input and generates a dictionary of 
    stacks of crates.
    """
    stack_dict = {}
    for line in layout_input:
        idx = 0
        for c in line:
            if is_crate(c):
                stack = idx_to_stack_num(idx) # Determine which stack this crate is on
                if (stack not in stack_dict): # Create stack if necessary
                    stack_dict[stack] = Stack()
                
                stack_dict[stack].push(c) # Push character onto top of stack
            idx += 1

    return stack_dict

MODE_9000 = 9000
MODE_9001 = 9001

def transfer_stack_top(stack_layout: dict, src: int, dest: int):
    """
    Transfers one item from the top of the stack at (src) to the stack at (dest).
    """
    item = stack_layout[src].pop()
    stack_layout[dest].push(item)

def process_instructions(instructions: list[Instruction], stack_layout: dict, process_mode: int):
    """
    Processes the instruction set and applies the changes to the given layout.
    """
    for instruction in instructions:
        if (process_mode == MODE_9000):
            for i in range(0, instruction.get_num_crates()):
                transfer_stack_top(stack_layout, instruction.src, instruction.dest)
        elif (process_mode == MODE_9001):
             
            # src to buffer
            transfer_buffer = []
            for _ in range(0, instruction.get_num_crates()):
                top_item = stack_layout[instruction.get_src()].pop()
                transfer_buffer.append(top_item)

            transfer_buffer.reverse() # Stacking order

            # buffer to src            
            for item in transfer_buffer:
                stack_layout[instruction.get_dest()].push(item)

def get_stack_top_summary(stack_layout: dict) -> str:
    """
    Returns the concatenation of the tops of each stack in the given layout dictionary.
    """
    msg = "" # Stores summary message
    col_order = [stack for stack in stack_layout.keys()]
    col_order.sort()
    for stack in col_order:
        if stack_layout[stack].get_size() > 0:
            msg += stack_layout[stack].peek()

    return msg

def extract_input_chunks(input: str) -> tuple:
    """
    Extracts data from the file with url (input) and returns in a tuple
    the layout input and the instructional input
    """
    LAYOUT = 1
    INSTRUCTION = 2
    parsing_mode = LAYOUT

    layout_input: list[str] = []
    instructions: list[Instruction] = []

    with open(input, 'r') as file:
        for line in file.readlines():
            if (line.isspace()):
                parsing_mode = INSTRUCTION
            elif (parsing_mode == LAYOUT):
                layout_input.append(line)
            elif (parsing_mode == INSTRUCTION):
                instructions.append(Instruction(line))

    layout_input.pop(len(layout_input) - 1) # Last line is useless for this approach
    layout_input.reverse() # Stacking order

    return (layout_input, instructions)


def day_five_puzzle_one(input: str):
    """
    Day 5: Puzzle #1 Solution Approach

    I have before me an input that may look like this:
        [D]    
    [N] [C]    
    [Z] [M] [P]
    1   2   3 

    move 1 from 2 to 1
    move 3 from 1 to 3
    move 2 from 2 to 1
    move 1 from 1 to 2

    I need to determine the top of each stack and return the sum.

    Part 1: parsing the input
    The initial layout and the instructions are separated by a blank line.
    I feel that it would be best to separately parse these contents. I will therefore separate
    the input into a layout input string, containing the layout lines, and then an instruction input
    string, containing the instruction lines.

    processing the layout:
    the last line, I know, will contain the number of elements to read for, so I can create a data
    structure, probably a dictionary of stacks mapped to stack #. Each element takes up 3 spaces.
    Each line can therefore be parsed by character amount, and the field extracted. Based on the character
    on the line, the element can be assigned to a stack column.

    Index relates to stack column by the following:
    1: 1
    2: 5
    3: 9    
    n: 4n - 3
    """
    input_chunks = extract_input_chunks(input)
    layout_input = input_chunks[0]
    instructions = input_chunks[1]
     
    stack_layout = generate_stack_layout(layout_input) # Generate dictionary of stacks
    process_instructions(instructions, stack_layout, MODE_9000) # Process and reassign stacks
    print(get_stack_top_summary(stack_layout)) # Determine tops and print out final message    

def day_five_puzzle_two(input: str):
    """
    Similar processing to part 1, and but with a different mode.
    """
    input_chunks = extract_input_chunks(input)
    layout_input = input_chunks[0]
    instructions = input_chunks[1]

    stack_layout = generate_stack_layout(layout_input) # Generate dictionary of stacks
    process_instructions(instructions, stack_layout, MODE_9001) # Process and reassign stacks
    print(get_stack_top_summary(stack_layout)) # Determine tops and print out final message

if __name__ == "__main__":
    test: str = "../input/day_five_puzzle_one_input_test.txt"
    input: str = "../input/day_five_puzzle_one_input.txt"

    day_five_puzzle_one(test) # PASS
    day_five_puzzle_two(test) # PASS
    day_five_puzzle_one(input)
    day_five_puzzle_two(input)
