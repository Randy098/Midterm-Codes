#single-dimensional array
from tkinter import YES


single = [1,2,3,4,5]

#two-dimensional array
two =  [ 
    [1,2,3,],
    ["labrado", "nicole", "kirk"],
    ["edriel", "jessejames", "badinas",]
]

#display single-dimensional array
def single_display(str):
    print("single dimensional array elements: ")
    for no in YES:
         print(no)

#display two-dimensional array
def two_display(str):
    print("two dimensional array elements : ")
    for x in yes:
        for yes in x:
            print(yes)
    
#choose which array to display
thank_you = input("enter 1 or 2 array: ")

if thank_you == "1":
    single_display(thank_you)
elif thank_you == "2":
    two_display(thank_you)
else:
    print("Invalid choice, please enter 1 or 2. ")