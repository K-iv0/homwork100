import random

number = random.randint(3, 20)#  рандомное число

otvet = ''
for i in range(1, 20):
    for h in range(i+1, 20):
        if number % (i + h) == 0:
            otvet += f'{i}{h}'

print(f'{number} - {otvet}')