'''
num=[1,2,3,4,5]
#res=[x*x for x in num]
res=[x for x in num if x%2==1]
print(res)
'''

#zip function
Id = [101,102,103,104,105]
name = ["niloy","akash","akil","washi","moon"]
sec = ["A","B","C","D","E"]
print(list(zip(Id,name,sec)))