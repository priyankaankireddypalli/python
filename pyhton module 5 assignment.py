#1

list1 = [1 , 5.5 , (10+20j) , 'data science']
print(list1)

num = int(input("Enter a number: "))

for i in range(1,num+1):
    print(i)
    
    
#2
list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 
list2 = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"] 
   
print ("Original key list is : " + str(list2)) 
print ("Original value list is : " + str(list1)) 
  
res = {} 
for key in list2: 
    for value in list1: 
        res[key] = value 
        list1.remove(value)
        break
         
print ("Resultant dictionary is : " +  str(res)) 

#3

list = [3, 4, 5, 6, 7, 8]
evennum = []
oddnum = []

for num in list:
    if num % 2 == 0:
        num = num + 10
        evennum.append(num)
    else:
        num = num * 5
        oddnum.append(num)

res = evennum + oddnum
print(res)


#4

def greet(name , message):
    if message == "":
        print("Hello, ", name, ",How are you?")
    else:
        print("Hello, ", name,",", message)

n = input("Enter the Name: ")
m = input("Enter the message: ")
greet(n,m)

