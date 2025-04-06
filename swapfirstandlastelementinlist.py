#way 1 to solve by using temp value

mylist=[12,10,25,35,96]
size=len(mylist)

temp=mylist[0]
mylist[0]=mylist[size-1]
mylist[size-1]=temp
print("values after swapping",mylist)

# without using temp value

mylist1=[20,30,40,50,60]

mylist1[0],mylist1[4]=mylist1[4],mylist1[0]
print("values after swapping",mylist1)

# using tupple

mylist2=[25,35,45,55,65]
get=(mylist2[4],mylist2[0])

mylist2[0],mylist2[4]=get

print("after swapping:",mylist2)

