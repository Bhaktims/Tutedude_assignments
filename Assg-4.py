'''
ASSIGNMENT 4:
Module 5: Files, Exceptions, and Errors in Python

Task 1: Read a File and Handle Errors
Problem Statement:  Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.
'''

file4 = None
try:
   file4 = open('sample.txt','r')
   print("Reading file content :")
   f_read1 = file4.readline()
   print("Line 1 :",f_read1)
   f_read2 = file4.readline()
   print("Line 2 :",f_read2)
except FileNotFoundError:
    print("Error,The file was not found, Please check file name!!")
except Exception as e:
    print("Error : ",e)
finally:
    if file4:
        file4.close()
        print("File Closed")

'''
Task 2: Write and Append Data to a File 
Problem Statement: Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.
'''
file5 = None

try:
    file5 = open("output.txt",'a')
    x = input("Enter your name :")
    fw = file5.write(x + "\n")
    file5 = open("output.txt", 'r')
    fr = file5.read()
    print(fr)
except Exception as e:
    print("Error :",e)
finally:
    if file5:
        file5.close()