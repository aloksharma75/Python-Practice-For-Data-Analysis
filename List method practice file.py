product_list = ["shirt", "pent", "tshirt","polo tshirt"]
print (product_list)

del product_list 

#first we are decide two new list 

my_list = ["fish","egg","tomato","chicken","egg","onion","oil"]
your_list = ["alok","sajjad","shihab","nayem","masum"]

#append one element in list 
my_list.append ("mutton")
print (my_list)

#insert a element in list
my_list.insert(2, "garlic")
print (my_list)

#now time to remove on element in list 
my_list.remove("fish")
print(my_list)

#hahaha now we pop a index in list 
my_list.pop(4)
print(my_list)

#index and list lenth
print(my_list.index("oil"))
print(len(my_list))

#count element in list 
print(my_list.count("egg"))

#assending sort methode
my_list.sort()
print(my_list)

#decending sort method
my_list.sort(reverse=True)
print(my_list)

#now time to copy list
new_list = my_list.copy()
print (my_list)

#extend list or add list
my_list.extend(your_list)
print(my_list)