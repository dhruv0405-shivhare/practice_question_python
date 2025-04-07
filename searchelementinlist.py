mylist=[2,5,6,9,7]
ele=7
flag=0

for i in mylist:
    if(i==ele):
        print("element found")
        flag=1
        break
if(flag==0):
    print("element not found")    