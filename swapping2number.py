# num1=10
# num2=20

num1=input("enter num1")
num2=input("enter num2")


print("value of num1 before swapping:",num1 )
print("value of num2 before swapping:",num2 )

# temp=num1
# num1=num2
# num2=temp
num1,num2=num2,num1
print("after swapping:",num1)
print("after swapping:",num2)
