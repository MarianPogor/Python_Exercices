# Because lists are a very important data type we will learn more
# about what we can do with lists

# We already know how to access items in a list by using their
# indexes

from operator import itemgetter 
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
fruits_sub_list = fruits[2:5]
print(fruits_sub_list)

print(fruits[-5:-1]) # notice that here "mango" will not be printed
# the index represent from where it starts and where it ends 

print(fruits[-5:])
# To get first the first 5 elements of a list we can do either:
print(fruits[:5])
print(fruits[0:5])

print(fruits[:])


numbers = list(range(0, 10))
# The numbers used for slicing are usually named: [from:to:step]
even_from_first_5 = numbers[1:5:2]
print(even_from_first_5)

# numbers[1:5:2] - explanation:
#         | | |
#         start from the second item which is "2" (numbers[0] is "1")
#           | |
#           take elements untill index 5 exclusive (aka. 4 inclusive)
#             |
#             take every 2nd (second) item
# The same way we can ask for every 3rd, 4th, ... item.
# The numbers used for slicing are usually named: [from:to:step]

# To get every second item from the whole list:
print(numbers[::2])

# We can even ask for items from the end setting step to -1
print(numbers[::-3]) # reversed list
print(numbers[::-2]) # every second item of a reversed list



things_to_do = ["hover", "iron", "dishes", "walk", "read book", "code"]

print("wrong order of doing things:")
for x in things_to_do:
    print(x)

print("correct order of doing things:")
for x in things_to_do[::-1]:
    print(x)


# Slicing lists might be confusing because of the many possibilities
# it gives us: from/to/setpping/backwards/forwards. Don't worry if
# you will need to comeback the the interactive shell again and again
# to remind your self how slicing works. I do it too all the time.

# exercise 1: create a list with months.
# a) print it forwards

print("Print forwards:")
for x in things_to_do:
    print(x)
	
# b) print it backwards
print("Print backwards:")
for x in things_to_do[::-1]:
    print(x, end =' ' )

# c) print sublist of winter months
month_lst = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'December']
#using itemgetter 
print(*itemgetter(0, 1, 11)(month_lst))


# d) print sublist of summer months reversed

print(*itemgetter(7, 6, 5)(month_lst))

# e) print months of II and III quater

for x in month_lst[3:9]:
    print(x)

# f) print odd months
print("Odd months:")
for x in month_lst[0:12:2]:
    print(x)
# g) print even months from march to october
print(" Even months from march to october:")
for x in month_lst[2:11:2]:
    print(x)

# exercise 2: A coder's work is mostly reading existing code. Read
# the commented code below and before running it, try to deduce what
# will be the output of the code. Write it down, run the code, how
# many list slices did you predict correctly?

# Answers will be attached as comment 
languages = ["C#", "Java", "Python", "JavaScript", "C", "C++", "Ruby"]

#1 here it will print from index 0 which is "C#" to index 1 which is "Java" -passed

print(languages[0:2])
# print(languages[:])

#2 from elem at index 0 to elem at index 3 (JavaScript)- passed
print(languages[:4])

#3 here it will print the last elem
print(languages[-1:])


# 4 from -5 elem to -1 - fail  
print(languages[-5:])

#5 here is print from 2 to 2 element - fail
print(languages[::2]) 

#6 here is printing from last element to first element - passed
print(languages[::-1])
#7 here is printing from the index -3 ("C") to last  element -fail

print(languages[::-3])


# exercise 3: Write a program which will ask the user for a number N.
# Then the program will compute the sum of all even numbers from
# 0 to N.

n=int(input("Enter n value:"))
sum=0
#starting from 0 to the input number that can  divided by 2 
for i in range(0,n+1,2):
    sum+=i
print(sum)

# exercise 4: Create a list with random numbers. Print only numbers
# greater than 10.

lst_random =[1,7,12,36,99,545]

for i in lst_random:
	if(i>10):
			print(i)

# exercise 5: Write a program whcih will ask the user for a number N
# and print numbers from 1, 2, 3, 4,... untill their sum exceeds N

n_=int(input("Enter n value:"))
sum_=0
#starting from 0 to the input number
for i in range(0,n_+1):
    sum_+=i
print(sum_)