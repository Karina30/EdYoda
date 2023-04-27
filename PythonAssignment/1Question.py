num_elements = int(input())
my_list = []
for i in range(num_elements):
    element = input()
    my_list.append(element)

sorted_list = sorted(my_list, key=lambda x: x[-2])

print(sorted_list)
