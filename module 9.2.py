first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [x for x in first_strings if len(x) > 5]
print((first_result[0:3]))
second_result = [len(x) == len(y) for x in first_strings for y in second_strings]
print(second_result)
third_result = [[len(x) == len(y) for x in first_strings for y in second_strings if len(x) // len(y) == 2]]
print(third_result)