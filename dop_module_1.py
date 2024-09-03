grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]] # list
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'} # set
slovar = {}
p = list(students) # поменять на лист
p.sort() # сортировать по алф.
slovar.update({p[0]:sum(grades[0])/len(grades[0]), p[1]:sum(grades[1])/len(grades[1]), p[2]:sum(grades[2])/len(grades[2]),
               p[3]:sum(grades[3])/len(grades[3]), p[4]:sum(grades[4])/len(grades[4])})
print(slovar)
