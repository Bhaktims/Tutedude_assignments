'''
Module 6: Data Structures and Strings in Python

Task 1: Create a Dictionary of Student Marks Problem Statement:
Write a Python program that:
1.Creates a dictionary where student names are keys and their marks are values.
2. Asks the user to input a student's name.
3. Retrieves and displays the corresponding marks.
4. If the student’s name is not found, display an appropriate message.

'''

stud_marks = {'Bhakti':90,'Manoj':95,'Anmay':99,'Malhar':90,'Avyaan':89,'Achintya':95}

name = input("Enter a Student name :")

if name in stud_marks:
    print(name,"'s marks = ",stud_marks[name])
else:
    print('Student name not found')

'''
Task 2: Demonstrate List Slicing 
Problem Statement: Write a Python program that:
1.   Creates a list of numbers from 1 to 10.
2.   Extracts the first five elements from the list.
3.   Reverses these extracted elements.
4.   Prints both the extracted list and the reversed list
 
'''

nlist = [1,2,3,4,5,6,7,8,9,10]
x = nlist[0:5:1]
print(" first five elements from the list ",x)
y = x[::-1]
print(" Reverse elements ",y)
print(" extracted list ",x,"reversed list",y)