# 1.length of longest word

a=[]
n=int(input("enter the number of elements:"))
for i in range(n):
    element=input("enter element"+str(i+1) +":")
    a.append(element)
max1=len(a[0])
temp=a[0]
for j in a:
    if (len(j)>max1):
        max1=len(j)
        temp=j
print('the longest word is:',temp)
# o/p:
# enter the number of elements:5
# enter element1:simple
# enter element2:is
# enter element3:better
# enter element4:than
# enter element5:complex
# the longest word is: complex
#
# Process finished with exit code 0

# 2.Quarks

class Quark(object):
    _color=frozenset(["red","blue","green"])
    _flavor=frozenset(["up","down","strange","charm","top","bottom"])
    baryon_number=1/3
    def __init__(self,color,flavor):
        if color in self._color:
            self.color=color
        else:
            raise ValueError(f"{color} is not allowed color for quarks!")
        if flavor in self._flavor:
            self.flavor=flavor
        else:
            raise ValueError(f"{flavor} is not allowed flavor for quarks!")
    def interact(self,quark):
        self.color,quark.color=quark.color,self.color


# 3.list of lists

def process_data(data):
    ret=1
    for x in data:
        ret *= x[0]-x[1]
    return ret
a=process_data([[2,5]])
b=process_data([[3,4]])
c=process_data([[8,7]])
print(a)
print(b)
print(c)

# o/p:
# -3
# -1
# 1
#
# Process finished with exit code 0

# 4.Vectors

class Vector(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def add(self,vector):
        return Vector(self.x+vector.x,self.y+vector.y)


o/p:
3
4

Process finished with exit code 0

# 5.Total amount of points

def points(games):
    count=0
    for score in games:
        res=score.split(':')
        if res[0]>res[1]:
            count+=3
        elif res[0]==res[1]:
            count+=1
    return count
s1=points(["3:1"])
s2=points(["2:2"])
s3=points(["0:1"])
print(s1)
print(s2)
print(s3)

# o/p:
# 3
# 1
# 0
#
# Process finished with exit code 0
