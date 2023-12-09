def format_line(line):
    return [int(x) for x in (line.strip()).split()]

def recursion(line):
    if all(element == 0 for element in line):
        return 0

    next_elements = []
    for i in range(len(line) - 1):
        next_elements.append(line[i+1] - line[i])
    return line[-1] + recursion(next_elements)
        
def main():
    summnation1 = 0
    summnation2 = 0

    with open('Day9.txt', 'r') as file:
        for i, line in enumerate(file):
            line = format_line(line)
            next_number = recursion(line)
            summnation1 += next_number
            next_number = recursion(line[::-1])
            summnation2 += next_number

    print("Part One", summnation1)
    print("Part Two", summnation2)


if __name__ == "__main__":
    main()


    
