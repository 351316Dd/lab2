#self study for
x=5
y=6
long = (x==x) and ((x[0]==5) or (x==0))
#the problem is that x is NOT a string which can not be indexed

long = (x==x) and ((x==5) or (x==0))
print (long)
# Ture becase 
# True and True 
# True and 'True or True'
# and: takes 1 False   or: takes 1 True 



my_list = ['a', 'b', 'c', 'd', 'e']
for letter in my_list:
    if letter == 'c':
        continue
    else:
        print('I see the', letter)
        print('Done with that iteration...')
print('Where did the "c" go?')
#This code will only print "I see the" followed by letters 
#that are not equal to 'c', 
#and it will print "Where did the 'c' go?" after the loop completes.

x=0
while x<5:
    print ('x is', x)
    x += 1 
#This is very handy in collecting user feedback
#you can trap the repsond until the right answer is enterd


while x < 5:
    print('x is', x)
    if x == 3:
        break
    x += 1
#this is not optimal as you would have to derviate manully 
#the fact that 3 + 1 =4

x = [10, 20, 30, 40, 50]

for val in x:

    print(val * 2)