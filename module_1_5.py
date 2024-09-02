immutable_var = 1,3,'s','p'
print(immutable_var)
# кортеж не поддерживаетизменение отдельного элемента в списке, кроме двух функций, сложение и умножение
# на нем стоит "защита" от изменения
immutable_var = (1,3,'s','p') + (5,'f') * 2
print(immutable_var)
mutable_list = [2,'5',6,'f']
mutable_list[1] = 4
mutable_list.remove(6)
mutable_list.extend(['a'])
print(mutable_list)