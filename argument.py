
#xargs
'''
def std(id):
    print(id)

std(101)
'''

'''
def std(id,name):
    print(id,name)

std(101,"washi")
'''
'''
def std(*detais):
    print(detais)

std(102,"akil",3.56,23)
'''
'''
def add(*num):
    sum=0
    for n in num:
        sum=sum+n
    print(sum)

add(12,34)
add(13,17,10)
add(20,10,50,20)
'''
#xxargs

def std(**detail):
    print(detail)

std(id=101,name="moon",cgpa=3.5,age=23)