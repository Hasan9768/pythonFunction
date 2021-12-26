try:
    n1= int (input("numer one"))
    n2= int (input("number two"))
    res= n1/n2
    print(res)

except ValueError:
    print("Only Integer")
except ZeroDivisionError:
    print("Impossible")
finally:
    print("Thanks")