my_dict = {'Ksenia': 2000,'Tany': 1997, 'Olrsy': 2001}
print(my_dict)
print(my_dict['Tany'])
print(my_dict.get('Polina'))
my_dict.update({'Maksim': 2003,
                'Roman': 1995})
a=my_dict.pop('Maksim')
print(a)
print(my_dict)
my_set = {1.67, 5, 're', 1.67, 3.78, 're', 6}
print(my_set)
my_set.add('fi')
my_set.add(45)
my_set.discard(1.67)
print(my_set)