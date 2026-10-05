input_file = open("checksum_input.txt", "r")
output_file = open("checksum_results.txt", "w")

checksum = 0

for line in input_file:
    numbers = line.strip().split()
    numbers = [int(number) for number in numbers]

    largest = max(numbers)
    smallest = min(numbers)
    difference = largest - smallest

    checksum += difference
    output_file.write(str(difference) + "\n")

output_file.write("Checksum: " + str(checksum))

input_file.close()
output_file.close()