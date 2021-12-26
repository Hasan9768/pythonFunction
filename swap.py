
a=23
b=43
'''
temp= a # temp=23
a= b # a=43
b= temp # b=23
'''
a,b=b,a
print("a= ",a)
print("b= ",b)