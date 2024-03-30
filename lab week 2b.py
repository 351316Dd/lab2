#Jiaxuan LIU
#Unless otherwise noted, try solving these using class content and without searching online


#Note for myself
#When given a list of integer, the element in the list can be used 
##as the index.
###for example:
####for val in my_list:
#####print (*(my_list[0:val]))
###### Without the * the result would be in the form of list []


#Note for myself
##When using continue function, the loop might be cut if the 
### skipped value is the "filling Piece" of the loop
####  elif i==5:
#    continue
# vs
####  elif i==5:
#     i+=1
#    continue
#Because if i=6 is skipped, the latter side of the code would not be triggered


#1
#Modify this code so that when i is 5 it doesn't print anything (including Finished!)
#and instead moves directly onto 6, while leaving it unchanged for other values of i
i = 0
while i < 10:
    if i < 5:
        print ('little')
    elif i>5:
        print('big')
    elif i==5:
        i+=1
        continue
    else:
        print('what happened?')
    print('Finished!')
    i+=1

#2
#Write a for loop that prints this pattern:
#HINT: you can write a for-loop inside of a for-loop

#1
#1 2
#1 2 3
#1 2 3 4


    
my_list = [1,2,3,4]
for val in my_list:
    print(*range(1, val + 1))

for val in my_list:
    print(*range(0,4))

i=0
while i < 4:
    print(my_list[:i+1])
    
i = 1
while i < 5:
    print(my_list[0:i])
    i += 1
#not in the form of value
i=1
while i<5:
    print(list(range(1,i+1)))
    i+=1

i = 1
while i < 5:
    print(*range(1, i + 1))
    i += 1
#Final Take!!!

my_list = [1,2,3,4]
for val in my_list:
    print (*(my_list[0:val]))
#Final Take 2

i = 1
my_list = [1,2,3,4]
while i < 5:
    print(*my_list[0:i])
    i += 1
#Final Take 3

#3
start_list = [[2, 3, 4], [6, 8, 9]]
#turn it into [1,    2,   3, 4   ]  
flat_list=[x for xs in start_list]
print(flat_list)

#attempt 2
flat_list=[x for sublist in start_list for x in sublist]
print(flat_list)

filtered_list = ['1','','2','3','4','', for x in flat_list if x == 2,3,4,6,8,9]

#attempt 3
filter_list = [1 if x == 2 else
               2 if x ==4 else
               3 if x == 6 else
               4 if x==8 else 
               '' 
              for x in flat_list]
print (filter_list)

#attempt 4 
filter_list = [round(x/2,0) if x!= 3 and x!= 9
               else " "
               for x in flat_list]
print (filter_list)

#attempt 4
filter_list = [int(x/2) if x!= 3 and x!= 9
               else " "
               for x in flat_list]
print (filter_list)

filter_list = [x if x != ' ' 
               else ' ' for x in filter_list]
print (filter_list)

#attempt 5
filter_list = [x for x in filter_list if x != " "]
print(filter_list)



#turn it into [1,    2,   3, 4   ]  
#NOTE:  The spacing is just to show which numbers are converted to which
#HINTS: There are three steps here: mapping, filtering, and flattening the nested lists
#       Try doing this in a for-loop, then try doing it in a list comprehension
#       You may need to check StackOverflow for how to flatten a nested list


#4
import datetime
start_dict = {'noah': '2/23/1999'   ,
              'sarah':'9/1/2001',
              'zach': '8/8/2005'}
capitalized_dict = {key.capitalize(): value for key, value in start_dict.items()}
print(capitalized_dict)

Datetime_cap = {key: datetime.datetime.strptime(value, '%m/%d/%Y') for key,
                value in capitalized_dict.items()}
print(Datetime_cap)

#attempt 2
Datetime_cap = {key: datetime.datetime.strptime(value, '%m/%d/%Y').date() for key,
                value in capitalized_dict.items()}
print(Datetime_cap)

#turn it into {'Noah': datetime.datetime(1999, 2, 23),
#              'Sarah': datetime.datetime(2001, 9, 1),
#              'Zach': datetime.datetime(2005, 8, 8)}
#HINTS: The datetime library has a function that turns strings of the right format into dates
#       Again, start with a for-loop, but make a dictionary comprehension in the end
