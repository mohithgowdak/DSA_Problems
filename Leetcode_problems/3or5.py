n=int(input())
n-=1
x=(n//3)*3
sum3=((n//3)/2)*(3+x)
y=(n//5)*5
sum5=((n//5)/2)*(5+y)
z=(n//15)*15
sum15=((n//15)/2)*(15+z)
print(int(sum3+sum5+sum15))
