
# part 2
def main():
    with open('input.txt') as f:
        lines = f.readlines()

        curr = 0
        cts = []
        for line in lines:
            if line == "\n":
                cts.append(curr)
                curr = 0

            else:
                curr += int(line)
                
            
        cts.sort(reverse=True)

        return cts[0], sum(cts[:3])

part1, part2 = main()