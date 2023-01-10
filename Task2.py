# 1.convert a number into a reversed array of digits

convertNta=lambda number : list(map(int,str(number)[::-1]))
print(convertNta(123456))

# o/p:
# [6, 5, 4, 3, 2, 1]

Process finished with exit code 0
# 2.sum of 2 smallest num

l=[19,5,42,2,77]
smallest=min(l)
l.remove(smallest)
smallest2=min(l)
l.remove(smallest2)
print(smallest+smallest2)

# o/p:
# 7
#
# Process finished with exit code 0

# 3.sum of 2 largest integer

l=[19,5,42,2,77]
largest=max(l)
l.remove(largest)
largest2=max(l)
l.remove(largest2)
print(largest+largest2)

# o/p:
# 119
#
# Process finished with exit code 0

# 5.invert values

def invert(lst):
    return[n*-1 for n in lst] if len(lst)>0 else[]
sa=invert([1,2,3,4,5])
print(sa)

# o/p:
# [-1, -2, -3, -4, -5]
#
# Process finished with exit code 0

# 6.How good are you really

def better_than_average(class_points,your_points):
    average=(sum(class_points)+(your_points) / (len(class_points)+1))
    return your_points < average
s1=better_than_average([2,3],5)
print(s1)
s2=better_than_average([41,75,72,56,80,82,81,33],50)
print(s2)

# O/p:
# True
# True
#
# Process finished with exit code 0

# 7.removing string spaces

def no_space(x):
    print (x.replace(" ",""))
(no_space('a n i m a l'))

# o/p:
# animal
#
# Process finished with exit code 0

# 8.shortest word

mypets=['cats','birds','fishes']
result=min(mypets,key=len)
print(result)

# o/p:
# cats
#
# Process finished with exit code 0

# 10. Are you playing banjo
data=int(input("enter the num:"))
for i in range (data):
    name=input("enter the name: ")
    if (name[0]==("R")) or (name[0]==("r")):
        print ("play banjo")
    else:
        print("does not play banjo")

# o/p:
# enter the num:3
# enter the name: sathish
# does not play banjo
# enter the name: raj
# play banjo
# enter the name: Raju
# play banjo
