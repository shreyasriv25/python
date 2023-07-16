list=[1,3,2,4,5,6,8,4,3]
print(list)

#add element
list.append(8)
print(list)

#remove element
list.pop()
print(list)

#sorting list
list.sort()
print(list)

#reverse sorting 
list.reverse()
print(list)

#min and max
print(max(list))
print(min(list))

#sum and avg of all elements
sum=0
for i in range(0,len(list)):
    sum=sum+list[i]
print(sum)
print(sum/len(list))

#remove duplicates
list1=set(list)
print(list1)


#index of an element
print(list.index(2))


#adding more than one element in a list

mylist= [1,3,4,2,6]
mylist.extend([8,9])
print(mylist)


#printing only integers from the list

list=['a',1,2,'4.0',True]
list1=[s for s in list if s.isdigit()]
print(list1)









