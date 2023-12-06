class Handle_Line:
    def __init__(self, line):
        lines = [x.split(" ") for x in (line.split(":")[1]).split("\n")[1:]]
        self._numerical_data = [[int(element) for element in row] for row in lines]

    def hande_one(x):
        for (destination, source, rge) in self._numerical_data:
            # check if that number is in the allocated range 
            if x >= source and x <= source + rge:
                
                # converstion 
                return x + distance - source
            
        #returning itself if it is not in this range 
        return x

    def handle_range(self, ranges):
        result = []
        for (destination, source, rge) in self._numerical_data:
            source_end = source + rge
            new_ranges = []
            
            while ranges:
                (start, end) = ranges.pop()

                #finding the sections of the ranges to appropriately apply next class 
                before = (start, min(end, source))
                
                overlap = (max(start, source), min(source_end, end))
                
                after = (max(source_end, start), end)

                #checking if sequences are valid to append to result
                if overlap[1] > overlap[0]:
                    result.append((overlap[0] - source + destination, overlap[1] - source + destination))

                #Adding to ranges to process again until it is suitable
                if before[1] > before[0]:
                    new_ranges.append(before)
                    
                if after[1] > after[0]:
                    new_ranges.append(after)
                    
            ranges = new_ranges
        return result + ranges

def main():
    input_data = open("d5.txt").read().strip()
    seeds, *data = input_data.split("\n\n")
    seeds = [int(x) for x in (seeds.split("seeds: ")[1]).split(" ")]

    #handle each line by creating it a class
    lines = [Handle_Line(line) for line in data]

    #list to store part 2 solutions 
    part_2 = []

    #split data from seed line into pairs for processing ranges
    pairs =  [(seeds[i], seeds[i + 1]) for i in range(0, len(seeds), 2)]
    for start, end in pairs:
        ranges = [(start, start + end)]
        
        for function in lines:
            ranges = function.handle_range(ranges)
            
        part_2.append(min(ranges)[0])
    
print(min(part_2))  


if __name__ == "__main__":
    main()
  
