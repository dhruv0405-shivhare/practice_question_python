# using list comprehension
mylist=[5,6,9,8,8,7]
mylist_copy=[i for i in mylist]
print(mylist_copy)

#using copy() method

mylist1=[5,9,6,3,5,58,]
mylist_copy1=mylist1.copy()
print(mylist1)

# using extend() method

mylist2=[5,6,9,32,6,4]
mylist_copy2=[]
mylist_copy2.extend(mylist2)
print(mylist_copy2)