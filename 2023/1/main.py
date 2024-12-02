import re, os

script_dir = os.path.dirname(os.path.realpath(__file__))
document_path = os.path.join(script_dir, 'calibration.txt')

# Number words mapping
number_words = {
    "one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
    "six": "6", "seven": "7", "eight": "8", "nine": "9", # Add more as needed
}

# Compile the regex pattern to find individual digits
number_pattern = re.compile(r'\d|' + '|'.join(number_words.keys()))

# Initialize a variable for the final total
final_total = 0

# Function to replace number words with digits
def replace_number_word(match):
    word = match.group(0)
    return number_words.get(word, word)

# Open and read the document line by line
with open(document_path, 'r') as file:
    for line in file:
        # Replace spelled-out numbers with digits
        print(final_total, line)
        line = number_pattern.sub(replace_number_word, line)
        # Find all digits in the line
        digits = re.findall(r'\d', line)
        print(digits)
        # Concatenate digits and convert to integer
        if digits:
            line_total = int(str(digits[0]) + str(digits[-1]))
            print(line_total)
        else:
            line_total = 0
        # Add the line total to the final total
        final_total += line_total

print(f"Final Total: {final_total}")


def star_1():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    document_path = os.path.join(script_dir, 'calibration.txt')

    # Compile the regex pattern to find individual digits
    pattern = re.compile(r'\d')

    # Initialize a variable for the final total
    final_total = 0

    # Open and read the document line by line
    with open(document_path, 'r') as file:
        for line in file:
            # Find all digits in the current line
            digits = pattern.findall(line)
            print(final_total, digits, line)
            # Concatenate digits and convert to integer
            if digits:
                line_total = int(str(digits[0]) + str(digits[-1]))
            else:
                line_total = 0
            # Add the line total to the final total
            final_total += line_total

    print(f"Final Total: {final_total}")