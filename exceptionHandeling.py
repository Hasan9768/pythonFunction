
'''
n2=int(input("Enter a number :"))
result = 20/n2
print(result)
print("Done")
'''
'''
text = "Diuan"
print(text[4])
print("success")
'''
'''
list = [20,0,10]
result = list[0]/list[2]
print(result)
print("Done")
'''

try:
    list = [20, 0, 10]
    result = list[0] / list[3]
    print(result)
    print("Done")

except ZeroDivisionError :
    print("Wrong input")

finally:
    print("Successfully")
print("Yes")

try:
    n1=int (input("number one: "))
    n2=int (input("number two: "))

     result = n1/n2
     print(result)

except ValueError:
           print("Integer only")
except ZeroDivisionError:
        print("Impossible")
finally:
     print("yes")








