# 1

# Creating 2 lists

lista = [1999 , 5.11 , 'Priya' , (5+1j) , True]
listb = [2005 , 5.11 , 'Preethi' , (6+2j) , False]

# Creating another list by concatination 

listc = lista + listb
print("After Concatination: ", listc)

# Finding the frequency of each element in concatinated list

import collections
frequency = collections.Counter(listc)
print("The frequency of each element in the list are: ", frequency)

# Printing the list in reverse order

listc.reverse()
print("Reversed list: ", listc)


# 2

# Creating two sets

seta = {1,2,3,4,5,6,7,8,9,10}
setb = {5,6,7,8,9,10,11,12,13,14,15}

# Finding the common elements in the above two sets

setc = seta.intersection(setb)
print("The common elements in both the sets are: ", setc)

# Finding the elements that are not common in both sets

setd = seta - setb
sete = setb - seta
x = setd.union(sete)
print("The elements that are not common in both the sets are: ", x)

# Removing 7 from both the sets

seta.discard(7)
print(seta)
setb.discard(7)
print(setb)



# 3
# Creating dictionary of 5 states as key and number of COVID cases as values

state = {'Karnataka' : 902000 , 'Telangana' : 278000 , 'Andhra Pradesh' : 875000 , 'Kerala' : 672000 , 'Tamil Nadu' : 800000}

# Printing only state names from the dictionary
print("States: ", state.keys())

# Updating another state and its COVID cases
del(state['Andhra Pradesh'])

state['Himachal Pradesh'] = 49000

print("After updating: ", state)
