'''
5!=5*4*3*2*1
4!=4*3*2*1
3!=3*2*1
2!=2*1
1!=1

5!=5*24=120
4!=4*6=24
3!=3*2=6
2!=2*1=2
1!=1
n!= n*(n-1)!

int fact(int n)
{
   // base case
if (n==1)
return 1;
else
return n*fact(n-1)
}
'''

def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)

print(fact(5))