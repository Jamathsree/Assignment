# 1.write a  program to interchange first and last element in a list 
def swapList(newList):
    newList[0],newList[-1] = newList[-1],newList[0]
    return newList

newList =[50,13,35,56,100]
print(swapList(newList))

# 2 wirte a program to find smallest number
list1 = [10,20,30,65,99]
list1.sort()

print("smallest Elemet is:",list1[0])

# 3 write a program to print even numbers in list 
list1 = [3,7,2,4,8,14,19,21]

for num in list1:
    
    if num%2 ==0:
        print("sum of even number in List:",num, end ="")
        
# 4 write a  program to print odd numbers in the list
start = int(input("Enter the start of range"))
end = int(input("Enter the end of range"))

for num in range(start,end+1):
    if num% 2 != 0:
        print(num)
        
# 5 wirte a program to print +ve numbers in list
list1 = [-10,21,-4,-45,-66,93]
num = 0
while(num<len(list1)):
    
    if list1[num] >= 0:
        print(list1[num])
        
    num += 1
# 6 wirte a program to print -ve numbers in list

list1 = [10,-21,-30,45,-50,-66]

for num in list1:
    if num <= 0:
        print(num)
        
# 7 Write a program to convert fahrenhit to celsius 
Fahrenheit = float(input("Enter the Fahrenheit numb:"))
Celsius = (Fahrenheit - 32)/1.8
print(Celsius)

#  8 write a program to print max and min number in tuple
tup = tuple()
num = int(input("Total num of valuues in tuple:"))
for i in range(num):
    x = input("enter the element:")
    tup =tup+(x,)
print("max value",max(tup))
print("mmini valve:",min(tup))

# 9 write a prython program to convert list to tuple
def convert(list):
    return tuple(list)

list = [1,23,4,5]
print(convert(list))

#10.  write a programm to create a list and use the following functons 1. append ,2.extend ,3. len()
list1 = ["Apple","ball","cat","dog"]
list1.append("orange")
print(list1)

list1 = ["Apple","ball","cat","dog"]
list2 = ["mango", "pineapple", "papaya"]

list1.extend(list2)
print(list1)
print(len(list1))