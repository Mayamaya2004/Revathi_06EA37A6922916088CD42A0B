i = []  
n = int(input("enter the no of elements in list:"))  
for x in range(0,n):  
    element=int(input("enter the element" + str(x+1) + ":"))  
    i.append(element)  
j=[sum(i[0:x+1]) for x in range(0,len(i))]  
print("Original list is: ",i)  
print("Cumulative sum list is: ",j)