### Python Summary ###

##LISTS

my_list = [1,2,3]

#Adding  items
my_list_new_item = my_list + [4]
my_list.append(4)

#Deleting items
del my_list[3] # use del to permamently delete an item

popped_item = my_list.pop() # use pop to delete an item from a list and return it --(last_in_first_out)
popped_item = my_list.pop(0) # use pop to delete an item from a list and return it--(first_in_first_out)

#change the item
my_list = [1,2,3]
my_list[2] = 5
print(my_list[2])

#Slicing
my_list = [1, 2, 3, 4, 5]
sliced_list = my_list [1:4]
print(sliced_list)


##DICTIONARIES (key value-each key is associated with a value)
house= {
  "kitchen": 5,
  "living_room": 12,
  "bedroom": 8
}
#Example: Calculate the whole surface of the house

surface = house["kitchen"] + house["living_room"] + house["bedroom"]
print(surface)


##IF CONDITION
my_condition = True
if my_condition == True:
  print("The condition was True")
  print("I could do things for example")
else:
  print("The condition was not True")
  print("I could do other things for example")
 
##LOOPS
my_list = [1, 2, 3, 4, 5]
for current_item in my_list:
  print(current_item)

#Example: Calculate the total amount
sales = [15, 20, 10, 25, 30]

#Bad way
total = sales[0] + sales[1] + sales[2] + sales[3] + sales[4]
print(total)

#Good way
total = 0
for current_sales in sales:
  total = total + current_sales
print(total)

##FUNCTIONS -- creating new function
def my_square(value):
  result = value**2
  return result
 
result1 = my_square(2)
result2 = my_square(4)
result3 = my_square(5)

print(result1, result2, result3)

#Example for functions and loops
sales = [12, 25, 30, 15, 80, 120, 200, 300, 115, 100]

def num_transactions_above_threshold(sales_data, threshold):
  """
  Calculate the number of items whose values are above a certain threshold
  sales_date: list of items to evaluate
  threshold: the given threshold
  """
  num_transactions = 0
  for current_sales in sales_data:
    if current_sales > threshold:
      num_transactions = num_transactions + 1
   
  return num_transactions

result = num_transactions_above_threshold(sales, 80)
print(result)
