first = 57
second = 59
third = 50
print(first)
print(second)
print(third)
if first == second == third:
    print(3)
elif (first == second != third or first != second == third
      or second == third != first or second != third == first):
    print(2)
else:
    print(0)