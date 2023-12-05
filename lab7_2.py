my_tuple = (1, 2, 3, 7, 8, 9, 15, 16, 17, 20)
sequences_list = []
current_sequence = []
for num in my_tuple:
    if not current_sequence or num == current_sequence[-1] + 1:
        current_sequence.append(num)
    else:
        if len(current_sequence) > 1:
            sequences_list.append(current_sequence)
        current_sequence = [num]
if len(current_sequence) > 1:
    sequences_list.append(current_sequence)
print(sequences_list)
