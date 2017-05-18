b_math = []
b_phys = []
b_russ = []

with open('4.4_input.txt') as input_file:
    for line in input_file:
        line = [float(i) for i in line.split(';')[1:]]
        b_math.append(line[0])
        b_phys.append(line[1])
        b_russ.append(line[2])
        print(sum(line) / len(line))

print(sum(b_math) / len(b_math), sum(b_phys) / len(b_phys), sum(b_russ) / len(b_russ))