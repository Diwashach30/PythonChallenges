##Create a Python program that reads a file containing a list of numbers (one number per line)
##and add all those numbers together. It then writes the sum of those numbers to another file called sum.txt.

    
def sum_numbers(input_file):
    try:
        with open(input_file, 'r') as file:
            numbers = file.readlines()
            total_sum = sum(int(number.strip()) for number in numbers)
        return total_sum
    except FileNotFoundError:
        print(f"The file {input_file} was not found.")
        return None
    except ValueError:
        print("The file contains invalid data that cannot be converted to integers.")
        return None


def write_sum_to_file(sum_result, output_file):
    if sum_result is not None:
        with open(output_file, 'w') as file:
            file.write(f"Sum of numbers: {sum_result}\n")


input_filename = 'numbers.txt'  # Input file containing the numbers
output_filename = 'sum.txt'     # Output file to store the sum

sum_result = sum_numbers(input_filename)
write_sum_to_file(sum_result, output_filename)

print(f"The sum has been written to {output_filename}.")

