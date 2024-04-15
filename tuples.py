#creating aa tuple
tuple_one = (10,20,30,40,50,60,70,80,90,100)
print(tuple_one)

#accessing using  indexing
print(tuple_one[-3])
print(tuple_one[2])
print(tuple_one[1:3])

#adding items into a tuple
#Tuples are immutable hence items cannot be added to it

#removing items from a tuple
removeElement = tuple_one[2]
print(removeElement)


#count occurence
item_searched = 40
count = 0

for item in tuple_one: 
 if item == item_searched: 
   count += 1

   print(count)
   print("The item " + str(item_searched) + " was found "+str(count)+" times") 


tuple2 = ((5,10),(15,20,25))
print(tuple2[1][0])

removeNum = tuple2[0]
print(removeNum)

