from sympy import *
#print pi
x = Symbol('x')
y=Symbol('y')
print x
a = Rational(1,2)
b=Rational(5,6)
c=a+b
print c
a=1.0/2

print a
a=x+y+x-y
print a
a.subs(x, 1)
print a
a=(x+y+x-6*y).subs(x,1).subs(y,2)
b=(x**3+y**3).subs(x,1).subs(y,2)
a=x**3+y**3
print a, "=", b
a=expand((x + y)**3)
print a
a=limit(sin(x)/x, x, 0)
print a
a=limit(1/x, x, oo)
print a
x = Symbol('x')
y = Symbol('y')
A = [[1,x], [y,1]]
print A[0][0]

