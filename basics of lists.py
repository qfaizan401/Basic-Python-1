#creation of list by list() func:
a = 'abcdefghi'
my_list = list(a)
print(my_list)

b=10,90,80,54,100
my_list = list(b)
print(my_list)

c=89.6,788.36,89.5,78.6
my_list = list(c)
print(my_list)

#creation of personalized list
my_list_of_cities = ['KHI','HYD','MPK','DIKhan','LHR']
print(my_list_of_cities)
print(f'\nWelcome to {my_list_of_cities[0]}')
print(f'\nWelcome to {my_list_of_cities[1]}')
print(f'\nWelcome to {my_list_of_cities[2]}')
print(f'\nWelcome to {my_list_of_cities[3]}')
print(f'\nWelcome to {my_list_of_cities[4]}')
print('Welcome to '+ my_list_of_cities[0])

ListOfInt = [1,2,34,5,6,78,97,90]
print(f'member of int list {ListOfInt[5]}')

ListOfFloats = [1.2,3.45,67.8,90.7]
print(f'member of float list {ListOfFloats[-3]}')

AnotherList = ['KHI',18000,67.84]
print(f'Elements of list are {AnotherList[-1],AnotherList[-2],AnotherList[-3]}')
#list is itself a datatype
print(type(AnotherList))
print(type(my_list_of_cities))
#list func:
my_list_of_cities.append('New York')
print(my_list_of_cities)

my_list_of_cities = my_list_of_cities + ['Sukkur','Nooribad']
print(my_list_of_cities)

ListOfInt = ListOfInt + [10,100]
print(ListOfInt)

my_list_of_cities.insert(2,181)
print(my_list_of_cities)

# Lists: Taking slices out of them
x = range(0,20,2)
listOfOdds = list(x)
print(listOfOdds)

print(listOfOdds[2:5])
reverse_slicing = listOfOdds[-1:-4]
print(reverse_slicing)

reverse_slicing = listOfOdds[-4 :-1]
print(reverse_slicing)

print(listOfOdds[4:])
print(listOfOdds[:4])

#Lists: Deleting and removing elements
#method 1 (universal method)
del listOfOdds[6]
print(listOfOdds)

#method 2 list's func
listOfOdds.remove(6)
print(listOfOdds)

listOfOdds.remove(listOfOdds[0])
print(listOfOdds)

#Lists: popping elements
x = range(0,20,2)
listOfOdds = list(x)
print(listOfOdds)
pop_element = listOfOdds.pop(5)
print(pop_element)
print(listOfOdds)