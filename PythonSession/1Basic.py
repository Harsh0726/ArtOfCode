#Print Statement
print("Hello World!")

#String 
myName = "Adithya"
print(myName)

#int
myAge = 23
print(myAge)

#float
price = 15.50
print(price)

#Array
marks = []

#Append = insert data
marks.append(50)
marks.append(65.50)
marks.append("Ab")

print(marks)

#Keyboard Input
name = input("Enter your name?")
print("Hello", name)


#Accepting only int
num1 = int(input("Num 01:"))
num2 = int(input("Num 02:"))

sum = num1 + num2

print("SUM is:", sum)

#Selection --> if/else
age = int(input("Enter your age"))

if(age<=20):
    print("Kid")
elif(age>20):
    print("Adult!")
else:
    print("Enter valid age")



#Function
def Hello():
    print("Python")

Hello() #Calling function



#Function with main
def getMarks():
    result = int(input("Marks:"))
    return result

def Main():
    print("Started!")

    MD = getMarks()
    print(MD)

if __name__ == "__main__":
    Main()

#Iteration
for count in range(11):
    print(count)