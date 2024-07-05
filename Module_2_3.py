my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
value = 0
while value < len(my_list):
    if my_list[value] > 0:
        print(my_list[value])
        value = value + 1
        continue
    if my_list[value] == 0:
        value = value + 1
        continue
    if my_list[value] < 0:
        break

# Как я понимаю, можно без continue:

# my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
# value = 0
# while value < len(my_list):
#     if my_list[value] > 0:
#         print(my_list[value])
#         value = value + 1
#     elif my_list[value] == 0:
#         value = value + 1
#     elif my_list[value] < 0:
#         break