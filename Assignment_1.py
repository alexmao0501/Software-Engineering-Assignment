

#2. Write a program that prints ‘Hello World’ to the screen.

print ('Hello World')

#3.	Write a program that prints a multiplication table for numbers up to 12.

for i in range(13):
    for j in range(13): 
        print("%s x %s = %s" % (i,j,i*j))

#4.	Write a function that tests whether a string is a palindrome and test it in your program

def is_Palindrome(str):
    if str == str[::-1]:
        return True
    else:
        return False

print (is_Palindrome("abba"))
print (is_Palindrome("maya"))

#5.	Write a function that combines two lists by alternatingly taking elements
def merge(al,bl):
    mergelist =[]
    for i in range(len(al)):
        mergelist.append(al[i])
        mergelist.append(bl[i])
    return mergelist


al = ['a','b','c']
bl = [1,2,3] 

print (merge(al,bl))


#6.	Write a function that computes the list of the first 100 Fibonacci numbers. 
def fib(n):
 
    f1 = 1
    f2 = 1
    if (n < 1):
        return 

    else:
        print(f1, end=" \n")
        for x in range(1, n):
            print (f2, end=" \n")
            next = f1 + f2
            f1 = f2
            f2 = next

fib(100)


#7.	Write a function that determines if a given year is a leap year
def leapYear(year):
 
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        print("Leap Year")
    else:
        print("Not Leap Year")

leapYear(2000)
leapYear(2023)