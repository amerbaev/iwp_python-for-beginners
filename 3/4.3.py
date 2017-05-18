count_dict = {}

with open('4.3_input.txt') as input_file:
    words = [s.lower() for s in input_file.read().split(sep=' ')]
    for word in words:
        if word not in count_dict:
            count_dict[word] = 1
        else:
            count_dict[word] += 1

word_max_freq = max(count_dict, key=count_dict.get)
print(word_max_freq, count_dict[word_max_freq])