# 1.symbols in reverse fasion

def print_symbol(number,symbol):
    for i in reversed(range(number)):
        for j in range(i+1):
            print(symbol,end="")
        print("\n")
print_symbol(11,"*")


#o/p:
# enter the numbers of rows:11
#***********

#**********

#*********

#********

#*******

#******

#*****

#****

#***

#**

#*


Process finished with exit code 0

#2.print_symbol

def print_symbol(number,symbol):
    if (symbol!="-"):
        for i in reversed(range(number)):
            for j in range(i+1):
                print(symbol,end="")
            print("\n")
print_symbol(11,"*")

# o/p:
# ***********
#
# **********
#
# *********
#
# ********
#
# *******
#
# ******
#
# *****
#
# ****
#
# ***
#
# **
#
# *


Process finished with exit code 0

# # 3.Print function

def print_symbol(number,symbol):
    if (len(symbol)<=1):
        for i in reversed(range(number)):
            for j in range(i+1):
                print(symbol,end="")
            print("\n")
print_symbol(11,"aa")


# o/p:
#
# Process finished with exit code 0

# 4.given range:

def test_range(n,start_num,end_num=0):
    return start_num <= n <= end_num if end_num >= start_num else end_num <= n <= start_num
print(test_range(12,0,36))
print(test_range(12,12,36))
print(test_range(120,0,36))

# o/p:
# True
# True
# False
#
# Process finished with exit code 0

# 5.divisible by num

data=int(input("enter the value: "))
for i in range (data):
    if i % 3==0 and i % 5==0:
        print("three and five")
        continue
    elif i % 3==0:
        print("three")
        continue
    elif i % 5==0 :
        print("five ")
        continue
    else:
        print(i)

# o/p:
# enter the value: 15
# three and five
# 1
# 2
# three
# 4
# five
# three
# 7
# 8
# three
# five
# 11
# three
# 13
# 14
#
# Process finished with exit code 0. 


# 6.outside of given range

def test_range(n,s,e):
    print (s > n > e if e < s else e > n > s)
(test_range(12,0,36))
(test_range(12,12,36))
(test_range(120,0,36))

#  o/p:
#  True
#  False
#  False
#
# Process finished with exit code 0



