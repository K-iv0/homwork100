my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
perem = 0
while perem < len(my_list):
    if my_list[perem] < 0:
        break
    if my_list[perem] > 0:
        print(my_list[perem])
    perem += 1
